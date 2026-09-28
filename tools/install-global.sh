#!/usr/bin/env bash
# Backward-compatible entry point for the cross-platform maintainer helper.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "${BUSPRO_PYTHON:-python3}" "$REPO/tools/install-global.py" "$@"
