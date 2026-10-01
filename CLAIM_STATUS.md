# CLAIM_STATUS

**Sweep:** 178 / PASS-2026-10-01-178
**Classification:** RESEARCH
**Claim level:** ≤ 1
**Head before this file:** `3cdbc2e3f7fdbdeae52540555365b3d80dc382ef`

## Capability states

| Capability | State |
|------------|--------|
| Classical W+λφ⁴ identities (`model.py`) | IMPLEMENTED |
| Two-mode ratio R = 2 on the reduction | IMPLEMENTED and TESTED |
| Truncated multimode Bloch scan | IMPLEMENTED; window test only (1.5 < R < 2.6) |
| Factor of two as a constant of nature | NOT CLAIMED |
| Device spectral stability / thrust / Ware freeze / CFT-X import | NOT CLAIMED |
| Loop branch `14J.5F.1-loop-correction` | NOT on main; not re-audited this sweep. Prior Actions failure 36100043944 stands. |

## Verification observed this sweep

- Selection: `random.SystemRandom` over 82 live search names. Draw: this repository.
- Local: `PYTHONPATH=src python3 -m pytest -q` on clone of `3cdbc2e3` — 11 passed, 0 failed.
- Actions: falsify.yml run [36881720661](https://github.com/beyond-repair/bloch-coherence-factor2/actions/runs/36881720661) success on `3cdbc2e3` (Sweep-173 claim-cap commit). Post-push run for Sweep-178 is not claimed here.
- Releases API: empty. Tags API: empty. No release tag created (a tag would not raise claim level).
- Archived flag: false.
- Docs drift closed: README layout now names `LINE_FREEZE.md` and `CLAIM_STATUS.md`, which already existed.

A claim file does not raise the claim level.
