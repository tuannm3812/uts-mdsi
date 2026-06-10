#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_DIR="${1:-${SCRIPT_DIR}/..}"

if [[ ! -d "${VAULT_DIR}" ]]; then
  echo "ERROR: Vault folder not found: ${VAULT_DIR}" >&2
  exit 1
fi

if command -v open >/dev/null 2>&1; then
  echo "Opening Obsidian vault at ${VAULT_DIR}"
  open -a Obsidian "${VAULT_DIR}"
  exit 0
fi

if command -v xdg-open >/dev/null 2>&1; then
  echo "Opening Obsidian vault via xdg-open at ${VAULT_DIR}"
  xdg-open "${VAULT_DIR}"
  exit 0
fi

echo "ERROR: No supported opener found (open or xdg-open)." >&2
echo "Open Obsidian manually and point it at: ${VAULT_DIR}" >&2
exit 1
