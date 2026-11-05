# Changelog

## 1.0.0 — first public release

- Two editions: `judge` (full) and `judge-flash` (light, under 8,000 characters for Custom GPTs and Gems).
- Instructions in English and Arabic, aligned in meaning; every edition replies in the user's language and dialect.
- Routes: Direct, Ideate, Personal, Quick, Standard, Deep and Plan, chosen by stakes and request type.
- Core rules: choosing is not authorizing; disagreement is not evidence; never invent facts, prices or sources.
- Deep-route risk scan across ten categories, with severity ranking, a low / expected / high table, and cash runway that excludes already-prepaid costs.
- Explicit handling of unworkable, impossible or joke ideas: say so first, then find the useful core and the cheapest test.
- Fairness guard for comparing options and people; the skill's own drafts are treated as proposals.
- Final self-check: recompute numbers, make "only"/"best" claims match the table, and make no execution remarks when no tool or request exists.
- References: `edge-cases.md`, `runtime-protocol.md`, `usage.md`; Codex metadata in `agents/openai.yaml`.
- The light edition is self-contained: essential rules for tools, delegation, handoff, ties and stakeholders are inline, so it works when pasted without its reference files. Both light editions stay under 8,000 characters, with a safety margin.
- The personal-decision example is conditioned on what the user shared, instead of an unqualified verdict.
- `agents/openai.yaml`: removed the unverified `policy.products` list; light editions now invoke `$judge-flash`.
- Repository: MIT license, logo, published evaluation records in `evals/`, and a GitHub Actions check (`scripts/validate.py`) for frontmatter, size limits, links and EN/AR file parity.
