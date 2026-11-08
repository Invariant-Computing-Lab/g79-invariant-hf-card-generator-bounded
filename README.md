# G79 — invariant-hf-card-generator

**Programme context.** Invariant Computing Lab / provenance and release tooling. This public candidate provides bounded utilities rather than a recovered original upstream project, independently verified research outcome or unconditional software licence. Audit outputs and release approvals remain separate.

**Status: PUBLICLY VISIBLE BOUNDED RESEARCH CANDIDATE / NEWLY IMPLEMENTED UTILITY.** This is NOT the original unrecovered upstream G79 repository, and is NOT a scientific validation or a public release authorization.

## Functionality

This standalone, standard-library Python utility implements the finite **`hf_card_generator`** check. It includes deterministic synthetic input, fail-closed behavior where appropriate, and self-contained unit tests.

```shell
python run.py --input sample.json
python -m unittest discover -v
```

The fixture result is **HOLD**. HOLD is the correct safe result for unresolved approval, license, or claim review gates.

## V7 target linkage

- Target code: `G79`
- Planned title: `invariant-hf-card-generator`
- Source plan: `Invariant_Yayin_Plani_V7_Teslim(6).html`
- Original scientific/rights limitation: Bağlandı≠doğrulandı; claim gate'in yanlış olumlu/olumsuz kontrolü ve dış kullanım benchmark'ı gerekir.
- Implementation date: 2026-10-20, independently authored bounded starting implementation, **not** an independent experiment or original recovered functionality.

## Boundaries

No protected clinical data, third-party weights, network calls, training, physical claims, or public posting. The proof, source lineage, rights and integration gates remain open.

## Installation and release engineering (0.1.1)

```sh
python -m pip install .
invariant-g79 --input sample.json
python -m unittest discover -v
```

Exit codes: 0 = this bounded check passed; 1 = invalid input or check failure; 2 = HOLD / unverified evidence. HOLD is not success. Wheels use the unique `invariant_v7_g79` module to avoid cross-package import collisions. Empty evidence, string booleans, invalid digests and unsafe Windows/POSIX paths are rejected. Human-signature authenticity cannot be proven by a JSON flag.

This engineering revision does not recover the original upstream implementation and does not resolve ownership, licensing or independent scientific validation.
## Verified packaging revision — 2026-10-20

18 bounded contract tests, wheel build, clean offline co-install and CLI checks. Not the complete original research product.

Runtime state: `PASS`. Rights and release approval are separate. See `RELEASE_VERIFICATION.json`. No paper or conference submission is included as a new software result.

## Hugging Face card publishing correction (no paid compute)

The standalone [public model-card repair utility](tools/repair_public_hf_model_cards.py) targets **only three** stale, already-public Humanization Tech model cards (`mri-feature-distance-cp08`, `ncl-fitted-research-cp08`, `rhythm-source-predictor-cp08`). It changes only the status and publication-route wording: it does not touch weights, repository visibility, licences, model evaluation or clinical claims.

On an authenticated local computer with the free `huggingface_hub` package, run it *without arguments* to review the unified diffs. The explicit `--apply` mode requires typing `APPLY-THREE` and verifies each README after commit. Never share access tokens in chat. This utility is **published as source code**, not executed against those Hugging Face repositories by this GitHub commit.
