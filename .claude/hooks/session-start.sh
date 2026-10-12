#!/bin/bash
# Installs the Python libraries the NPO agent needs (scans, Word, Excel, charts).
# Only runs in Claude Code on the web; idempotent.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
python3 -m pip install --quiet --disable-pip-version-check -r requirements.txt
echo "export PYTHONPATH=\"$CLAUDE_PROJECT_DIR/tools${PYTHONPATH:+:$PYTHONPATH}\"" >> "$CLAUDE_ENV_FILE"
