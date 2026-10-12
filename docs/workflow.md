# Technical notes

## Downloading from Drive

`download_file_content` returns base64. Large files are saved by the harness
to a JSON file under `tool-results/`. Decode it like this:

```python
import json, base64
d = json.load(open(saved_path))
open("file.pdf", "wb").write(base64.b64decode(d["content"]))
```

The Python packages are listed in `requirements.txt`. In Claude Code on the
web, the SessionStart hook (`.claude/hooks/session-start.sh`) installs them
automatically and puts `tools/` on `PYTHONPATH`. Locally, run:

```
pip install -r requirements.txt
```

Render scan pages at about 110 dpi to read them, and crop at 220–300 dpi for
handwriting.

## Uploading

- A Google Doc is created with `create_file(textContent=<html>,
  contentMimeType="text/html", parentId=<case folder>)`.
- The .docx (about 1.3 MB because of the letterhead images) is too large to
  pass through the connector, so send it to the user with `SendUserFile`.

## LibreOffice

In the cloud container, LibreOffice can't open files. Don't rely on it to
recalculate `Normen.xlsx`. Reimplement the formulas instead, and prove the
reimplementation by reproducing the cached values in the workbook.

## Case scripts

Per case, write two small scripts in the scratchpad:

- `score_<ID>.py`: case facts, plus norms from `tools/normen_xlsx.py`, gives `scores_<ID>.json`
- `content_<ID>.py`: report text from the scores, gives `content_<ID>.json` for `tools/build_report.py`

Upload both to the case folder as `claude_werkbestand_*.py`. After feedback,
the next session downloads them, changes them and rebuilds the report.
