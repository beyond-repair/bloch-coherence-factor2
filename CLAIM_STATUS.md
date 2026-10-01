# CLAIM_STATUS

**Sweep:** 173 / PASS-2026-10-01-173
**Classification:** RESEARCH
**Claim level:** ≤ 1
**Head before this file:** `05571476be6510444a359c93b8e8243d30d9d826`

## Capability states

| Capability | State |
|------------|--------|
| Classical W+λφ⁴ identities (`model.py`) | IMPLEMENTED |
| Two-mode ratio R = 2 on the reduction | IMPLEMENTED and TESTED |
| Truncated multimode Bloch scan | IMPLEMENTED; window test only (1.5 < R < 2.6) |
| Factor of two as a constant of nature | NOT CLAIMED |
| Device spectral stability / thrust / Ware freeze / CFT-X import | NOT CLAIMED |
| Loop branch `14J.5F.1-loop-correction` | NOT on main; latest observed Actions run on that branch failed (36100043944). Not re-audited. |

## Verification observed this sweep

- Local: `PYTHONPATH=src python -m pytest -q` on clone of `05571476` — 11 passed, 0 failed.
- Actions: falsify.yml run [36844364901](https://github.com/beyond-repair/bloch-coherence-factor2/actions/runs/36844364901) success on `05571476` (before this file). Post-push run is not claimed here.
- Releases API: empty.
- Archived flag: false.

A claim file does not raise the claim level.
