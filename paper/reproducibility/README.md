# Reproducibility – Veritas Engine

This folder contains minimal scripts to reproduce Veritas Engine
results from timestamp-only JSON inputs.

All outputs are deterministic and hash-verifiable.
No content, no identities, metadata-only.
## How to Reproduce

1. Copy `input.example.json` → `input.json`
2. Paste full reply timestamps
3. Run:

```bash
python3 run_veritas.py