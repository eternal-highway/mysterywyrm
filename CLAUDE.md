# mysterywyrm

Working notes for agent sessions on this repo. Read before concluding anything
is impossible.

## What this repo points at

`README.md` holds one URL. It is the entry point to a literary project — an
alphabet book built on the Old English Rune Poem — spread across three domains:

| Domain | Role |
| --- | --- |
| `lettersfortitles.com` | the alphabet book itself; per-rune pages, riddles, `/the-middle/` |
| `alltimesticking.com` | sister site; tags incl. Marinetti, Molly Bloom, *mors certa hora incerta* |
| `slyuses.com` | anagram of **Ulysses** |

There is no code here. Treat the repo as a pointer, and the sites as the
primary sources.

## Network: probe before declaring a wall

Sessions run in an Anthropic cloud environment whose default access level is
**Trusted** — an allowlist of package registries, GitHub and cloud SDKs. The
three domains above are *not* on it, so every client gets a proxy refusal.

Do not report "blocked" on one tool's failure. Run the ladder
(`scripts/probe-net.sh <domain>`) and read the failure class:

| Symptom | Means | Do |
| --- | --- | --- |
| `CONNECT tunnel failed, response 403` | org egress policy | report the host; **do not route around it** |
| `405 Method Not Allowed` | tool sent plain HTTP | unset `HTTP_PROXY` for that tool |
| cert / PKIX error | tool ignores the CA bundle | point it at `/root/.ccr/ca-bundle.crt` |
| timeout, no proxy error | client ignores `HTTPS_PROXY` | use the tool's own proxy option |

Always establish a control: if `github.com` tunnels, the box is online and the
issue is the allowlist, not connectivity.

`/root/.ccr/README.md` documents every failure class. `curl -sS
"$HTTPS_PROXY/__agentproxy/status"` reports live proxy state. Both were
available and unread during the session that produced this file.

**Never** disable TLS verification, unset `HTTPS_PROXY`, or launder a blocked
request through an archive, cache or text-extraction relay. A 403 is the
policy working.

## To unblock

Edit the cloud environment (in the client: **⋯ → Edit environment**), set
network access `Trusted` → **Custom**, add:

```
lettersfortitles.com
*.lettersfortitles.com
alltimesticking.com
slyuses.com
```

Tick *"Also include default list of common package managers"* or npm/PyPI die.
Takes effect on **new** sessions only — the running VM's proxy config is fixed.

## Browser is already here

Chromium and Playwright ship in the image. No `playwright install`.

```
/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # real binary
/opt/node22/bin/playwright                           # CLI
```

Gotcha: `/opt/pw-browsers/chromium` is a symlink *to the binary*, not to a
directory — appending `chrome-linux/chrome` gives `Not a directory`.

Once domains are allowlisted, drive it properly (`--dump-dom`, screenshots,
crawl the rune index) instead of relying on search snippets.

## What cannot be worked around

No visibility into the user's client UI. Agent sessions cannot see the desktop
app, its menus, or its dropdowns; documentation is a poor substitute and was
wrong-footed once already. Ask, or ask for a screenshot.

## Structural work already done

The futhorc has **29** stanzas — odd, so mirroring inward from both ends gives
14 pairs and one unpaired centre. The site states the conceit: pairs mirrored
end-to-middle, `feoh`/`ear` as alpha and omega.

Reconstructed pairing (from the standard poem, *not* yet checked against the
site — divergences are the interesting part):

```
 1 feoh  wealth        ↔ 29 ear   the grave
 2 ur    aurochs       ↔ 28 ior   river-beast
 3 þorn  thorn         ↔ 27 yr    bow
 4 os    mouth/speech  ↔ 26 æsc   ash, withstands attack
 5 rad   the road      ↔ 25 ac    oak, tested on the sea
 6 cen   torch         ↔ 24 dæg   day
 7 gyfu  gift          ↔ 23 eþel  ancestral estate
 8 wynn  joy           ↔ 22 ing   who departed east
 9 hægl  hail          ↔ 21 lagu  the sea
10 nyd   need          ↔ 20 mann  man
11 is    ice           ↔ 19 eh    horse
12 ger   harvest       ↔ 18 beorc birch, fruitless
13 eoh   yew           ↔ 17 tir   the star
14 peorð untranslatable↔ 16 sigel the sun
                 15 eolhx  ← centre
```

Two load-bearing observations:

- **`eolhx` at dead centre** wounds whoever grasps at it (*wundaþ grimme*),
  echoing `þorn` at position 3. Its rune ᛉ also carried a sound actively dying
  out of the language (/z/ → /r/, final position only). A letter that cannot be
  held, at the centre of a book about letters.
- **`feoh`/`ear`** — wealth against the grave — is *mors certa hora incerta*
  in Old English: the sister site's Latin tag and this book's alpha-omega pair
  are one idea in two languages.

Next: `peorð`. The one stanza scholars cannot translate, sitting one step off
centre, mirrored against the sun.
