#!/usr/bin/env bash
#
# Integrity guard for the imported canonical corpus seed.
#
# The seed tree is a release payload: it must reproduce its own
# MANIFEST.sha256 byte for byte. Neither of the seed's own verifiers checks
# that, so without this guard an edit inside corpus-seed/ would pass both
# while silently invalidating the release.
#
# This script lives OUTSIDE corpus-seed/ on purpose. Anything added inside
# that tree would itself have to appear in the manifest.
#
# Checks, in order:
#   1. every manifest hash verifies;
#   2. the manifest's path set equals the tree's path set, except for the
#      manifest itself (derived dynamically -- no count is hardcoded, so a
#      future release with a different payload size still passes);
#   3. the Rune Code state verifier;
#   4. the filename letter-run verifier.
#
# Usage:  tools/verify-corpus-seed.sh
# Exit:   0 all checks pass; 1 on the first failure.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SEED_DIR="${REPO_ROOT}/corpus-seed"
MANIFEST="MANIFEST.sha256"

status=0
fail() { printf '  FAIL  %s\n' "$*"; status=1; }
pass() { printf '  ok    %s\n' "$*"; }

if [ ! -d "${SEED_DIR}" ]; then
    echo "corpus-seed/ not found at ${SEED_DIR}" >&2
    exit 1
fi

cd "${SEED_DIR}" || exit 1

if [ ! -f "${MANIFEST}" ]; then
    echo "${MANIFEST} not found in corpus-seed/" >&2
    exit 1
fi

echo "corpus-seed integrity guard"
echo "  tree: ${SEED_DIR}"
echo

# --- 1. hashes -------------------------------------------------------------

check_out="$(sha256sum -c "${MANIFEST}" 2>&1)"
check_rc=$?
manifest_entries="$(grep -c '' <<<"${check_out}")"
bad="$(grep -v ': OK$' <<<"${check_out}" || true)"

if [ ${check_rc} -eq 0 ] && [ -z "${bad}" ]; then
    pass "${manifest_entries} manifest hashes verify"
else
    fail "manifest hash mismatch"
    printf '%s\n' "${bad}" | sed 's/^/        /' | head -40
fi

# --- 2. path-set equality (derived, never hardcoded) -----------------------

tree_paths="$(find . -type f | sed "s|^\./|./|" | sort)"
manifest_paths="$(sed 's/^[0-9a-f]\{64\}  //' "${MANIFEST}" | sort)"
# The manifest cannot cover itself; that one path is the expected difference.
expected_uncovered="./${MANIFEST}"

untracked="$(comm -23 <(printf '%s\n' "${tree_paths}") <(printf '%s\n' "${manifest_paths}"))"
missing="$(comm -13 <(printf '%s\n' "${tree_paths}") <(printf '%s\n' "${manifest_paths}"))"

if [ "${untracked}" = "${expected_uncovered}" ]; then
    pass "every payload file is covered; only ${MANIFEST} is uncovered, as expected"
else
    fail "unexpected files present in the tree but absent from ${MANIFEST}:"
    comm -23 <(printf '%s\n' "${tree_paths}") <(printf '%s\n' "${manifest_paths}") \
        | grep -vxF "${expected_uncovered}" | sed 's/^/        /' | head -40
fi

if [ -z "${missing}" ]; then
    pass "no manifest entry is missing from the tree"
else
    fail "files listed in ${MANIFEST} but absent from the tree:"
    printf '%s\n' "${missing}" | sed 's/^/        /' | head -40
fi

# --- 3 & 4. the release's own state verifiers ------------------------------

for verifier in 05_method/verify_rune_code_state.py 05_method/verify_cipher_letter_run.py; do
    if [ ! -f "${verifier}" ]; then
        fail "${verifier} not found"
        continue
    fi
    if out="$(python3 "${verifier}" 2>&1)"; then
        pass "${verifier}"
        printf '%s\n' "${out}" | sed 's/^/        /'
    else
        fail "${verifier} exited non-zero"
        printf '%s\n' "${out}" | sed 's/^/        /'
    fi
done

echo
if [ ${status} -eq 0 ]; then
    echo "corpus-seed OK: payload reproduces ${MANIFEST} and both state verifiers pass."
else
    echo "corpus-seed FAILED. The imported tree must reproduce its release payload"
    echo "exactly; corrections belong outside corpus-seed/ or in a new corpus"
    echo "release with a regenerated manifest. See LINEAGES.md."
fi
exit ${status}
