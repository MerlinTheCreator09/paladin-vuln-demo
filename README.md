# paladin-vuln-demo

**Intentionally insecure test fixture** for the Paladin scanner (Manipal Hackathon 2026).
Every weakness below is planted on purpose so Paladin has something to find. All
"secrets" are obvious fake placeholders. **Do not deploy this. Do not copy this code.**

## Planted weaknesses (what Paladin should flag)

| File | Line area | Weakness | CWE |
|------|-----------|----------|-----|
| `app/server.py` | `API_KEY = ...` | Hard-coded credential (fake) | CWE-798 |
| `app/server.py` | `DB_PASSWORD = ...` | Hard-coded credential (fake) | CWE-798 |
| `app/server.py` | `execute("... " + uid)` | SQL built from string concatenation | CWE-89 |
| `app/server.py` | `eval(expr)` | Dynamic code execution of user input | CWE-95 |
| `app/server.py` | `os.system("ping ... " + host)` | OS command injection via the shell | CWE-78 |
| `app/server.py` | `app.run(debug=True)` | Debug mode enabled | CWE-489 |
| `web/index.html` | `<script src="http://...">` | Script loaded over plain HTTP | CWE-829 |
| `web/index.html` | `target="_blank"` (no `rel`) | Reverse tabnabbing | CWE-1022 |
| `requirements.txt` | pinned old versions | Known-vulnerable dependencies (OSV) | — |

That is **8 code findings + 2 vulnerable dependencies** across 3 files, so a scan should
produce real attack paths and give the fixers / agent something to remediate.
