# AgentNaomi

A Claude agent that handles the paperwork after a neuropsychological
assessment.

## How it works

1. Make an anonymous folder `cases/<CASEID>/` and name its files as
   described in [`docs/naming-convention.md`](docs/naming-convention.md).
2. Open Claude Code in this repo and say *"process case &lt;CASEID&gt;"*.
3. The agent checks the folder and scores every test with
   `tools/score_case.py`, which is plain code, so the model never does the
   math. It then summarises the documents and writes a draft report to
   `cases/<CASEID>/output/`.
4. She reviews the draft, fixes it, and signs off.

## Privacy

- `cases/` is git-ignored. Patient data stays on her machine and never
  reaches GitHub. Only the fictional `EXAMPLE-*` cases are tracked.
- Keep this repository **private**. The norm tables may be copyrighted.

## Try it

```
python3 tools/score_case.py cases/EXAMPLE-001
python3 -m unittest discover -s tests
```

## Layout

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Rules the agent always follows |
| `.claude/skills/process-case/` | Step-by-step case workflow |
| `docs/naming-convention.md` | File naming and what each file type is for |
| `tools/` | Scoring engine (norm lookup, z / percentile / T / scaled, classification) |
| `norms/` | Norm data and classification labels (**currently fictional examples**) |
| `templates/` | Report template (**placeholder**) |
