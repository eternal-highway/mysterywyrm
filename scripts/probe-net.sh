#!/usr/bin/env bash
# Probe a host before declaring it unreachable.
#
# Distinguishes org egress policy from tool misconfiguration from an actual
# outage. Run this instead of trusting one client's failure.
#
#   ./scripts/probe-net.sh lettersfortitles.com

set -uo pipefail

HOST="${1:?usage: probe-net.sh <domain>}"
CONTROL="${2:-github.com}"
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome

hr() { printf '%s\n' "------------------------------------------------------------"; }

probe() {
  curl -sS -o /dev/null -w "http=%{http_code}" --max-time 15 "https://$1/" 2>&1 \
    | tr -d '\n'
}

hr
echo "target : $HOST"
echo "control: $CONTROL"
hr

printf 'curl   %-24s ' "$HOST";    probe "$HOST";    echo
printf 'curl   %-24s ' "$CONTROL"; probe "$CONTROL"; echo

hr
echo "proxy state:"
curl -sS "${HTTPS_PROXY:-http://127.0.0.1:43821}/__agentproxy/status" 2>&1 \
  | head -c 600
echo
hr

if [ -x "$CHROME" ]; then
  echo "chromium:"
  timeout 45 "$CHROME" --headless=new --disable-gpu --no-sandbox \
    --dump-dom --virtual-time-budget=8000 "https://$HOST/" 2>&1 \
    | grep -oE 'ERR_[A-Z_]+' | head -1 || echo "  (no ERR_ code — page may have loaded)"
else
  echo "chromium: not found at $CHROME"
fi

hr
cat <<'EOF'
Reading the result:

  403 CONNECT on target, control connects
      -> org egress allowlist. Report the host. Do NOT route around it.
         Fix: Edit environment -> network access Custom -> add the domain.

  both fail
      -> proxy or network down, not a per-domain policy.

  405
      -> plain-HTTP request; unset HTTP_PROXY for that tool.

  cert / PKIX
      -> point the tool at /root/.ccr/ca-bundle.crt

  timeout, no proxy error
      -> client ignores HTTPS_PROXY; use its own proxy option.

Full failure-class reference: /root/.ccr/README.md
EOF
