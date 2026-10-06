# CLAIM_STATUS

**Sweep:** 245 / PASS-2026-10-06-245
**Classification:** RESEARCH
**Claim level:** ≤ 1
**Head observed:** `77d7063a51784be5ac6e39ca3a616dc73fa578c2`
**Prior claim file:** Sweep-178 on the same head. This file does not raise the claim level.

## Capability states

| Capability | State |
|------------|--------|
| Classical W+λφ⁴ identities (`model.py`) | IMPLEMENTED |
| Two-mode ratio R = 2 on the reduction | IMPLEMENTED and TESTED |
| Truncated multimode Bloch scan | IMPLEMENTED; window test only (1.5 < R < 2.6) |
| Factor of two as a constant of nature | NOT CLAIMED |
| Device spectral stability / thrust / Ware freeze / CFT-X import | NOT CLAIMED |
| Loop branch `14J.5F.1-loop-correction` | Present at `09f6902b8a3e30e603a2b85b6a5bc919b2611cb1`. Not merged. Not re-run this sweep. Prior Actions failure 36100043944 stands. |

## Verification observed this sweep

- Selection: `random.Random(20261006_1700).choice` over the 83-name search payload (`total_count` 83, `incomplete_results` false). Draw: this repository.
- Tree: 31 paths. Workflow `.github/workflows/falsify.yml` runs `PYTHONPATH=src pytest` on Python 3.12.
- Local: `PYTHONPATH=src python3 -m pytest -q` on clone of `77d7063a` — 11 passed, 0 failed.
- Actions: falsify.yml run [36897260976](https://github.com/beyond-repair/bloch-coherence-factor2/actions/runs/36897260976) success on `77d7063a` (Sweep-178 docs commit). No newer main run exists. Post-push run for Sweep-245 is not claimed here.
- Releases API: empty. Tags not created. A tag would not raise claim level.
- Archived flag: not flipped.
- Branches: `main`, `14J.5F.1-loop-correction` only.

A claim file does not raise the claim level.
