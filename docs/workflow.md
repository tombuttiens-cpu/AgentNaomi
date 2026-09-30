# Technical notes

## Downloading from Drive

`download_file_content` returns base64. Large files are saved by the harness
to a JSON file under `tool-results/`. Decode it like this:

```python
import json, base64
d = json.load(open(saved_path))
open("file.pdf", "wb").write(base64.b64decode(d["content"]))
```

The Python packages needed are `pymupdf` (render scans to PNG), `python-docx`,
`openpyxl` and `xlrd`:

```
pip install pymupdf python-docx openpyxl xlrd
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
