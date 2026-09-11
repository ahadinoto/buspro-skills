#!/usr/bin/env bash
#
# Dev helper for the maintainer. Symlinks skills from this working tree into the
# global skills directories that already exist on this machine, so edits are
# live in every agent with no reinstall step.
#
# This is NOT the mentee install path — mentees use `npx skills add` (see
# README.md), which pins a clone rather than following your uncommitted edits.
#
# Usage:
#   tools/install-global.sh                     # link every skill
#   tools/install-global.sh basecamp-todo-coach # link one skill
#   tools/install-global.sh --list              # show skills in this repo
#   tools/install-global.sh --unlink [skill]    # remove the links
#   tools/install-global.sh --dry-run [skill]   # show what would change
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO/skills"

# Candidate global skills directories. Only ones that already exist are
# touched — agent install paths change often, and creating a directory for an
# agent the user has not installed just leaves litter.
CANDIDATES=(
  "$HOME/.agents/skills"            # shared location, read by several agents
  "$HOME/.claude/skills"            # Claude Code
  "$HOME/.codex/skills"             # Codex
  "$HOME/.codeium/windsurf/skills"  # Windsurf
  "$HOME/.gemini/skills"            # Gemini CLI / Antigravity
  "$HOME/.cursor/skills"            # Cursor
)

UNLINK=0
DRY_RUN=0
LIST=0
REQUESTED=()

for arg in "$@"; do
  case "$arg" in
    --unlink)  UNLINK=1 ;;
    --dry-run) DRY_RUN=1 ;;
    --list)    LIST=1 ;;
    -h|--help) sed -n '2,16p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*) echo "unknown option: $arg" >&2; exit 2 ;;
    *)  REQUESTED+=("$arg") ;;
  esac
done

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "error: no skills/ directory at $SKILLS_DIR" >&2
  exit 1
fi

# Every directory under skills/ that actually holds a SKILL.md.
ALL_SKILLS=()
for d in "$SKILLS_DIR"/*/; do
  [[ -f "$d/SKILL.md" ]] || continue
  ALL_SKILLS+=("$(basename "$d")")
done

if [[ ${#ALL_SKILLS[@]} -eq 0 ]]; then
  echo "error: no skills found under $SKILLS_DIR (each needs a SKILL.md)" >&2
  exit 1
fi

if [[ $LIST -eq 1 ]]; then
  echo "Skills in this repo:"
  for s in "${ALL_SKILLS[@]}"; do echo "    $s"; done
  exit 0
fi

# Validate any explicitly requested names before touching anything.
if [[ ${#REQUESTED[@]} -gt 0 ]]; then
  for want in "${REQUESTED[@]}"; do
    found=0
    for s in "${ALL_SKILLS[@]}"; do [[ "$s" == "$want" ]] && found=1; done
    if [[ $found -eq 0 ]]; then
      echo "error: no skill '$want' in $SKILLS_DIR" >&2
      echo "       available: ${ALL_SKILLS[*]}" >&2
      exit 1
    fi
  done
  SKILLS=("${REQUESTED[@]}")
else
  SKILLS=("${ALL_SKILLS[@]}")
fi

run() {
  if [[ $DRY_RUN -eq 1 ]]; then
    echo "    would run: $*"
  else
    "$@"
  fi
}

dirs_found=0
for dir in "${CANDIDATES[@]}"; do
  [[ -d "$dir" ]] && dirs_found=$((dirs_found + 1))
done

if [[ $dirs_found -eq 0 ]]; then
  echo "No global skills directory found. Install an agent first, or create one:" >&2
  echo "  mkdir -p ~/.claude/skills && $0" >&2
  exit 1
fi

for skill in "${SKILLS[@]}"; do
  source_dir="$SKILLS_DIR/$skill"
  echo "$skill"
  for dir in "${CANDIDATES[@]}"; do
    [[ -d "$dir" ]] || continue
    target="$dir/$skill"

    if [[ $UNLINK -eq 1 ]]; then
      if [[ -L "$target" ]]; then
        echo "  unlink $target"
        run rm "$target"
      elif [[ -e "$target" ]]; then
        # A real directory here is someone's `npx skills add` install, or a copy
        # with edits in it. Deleting it could lose work, so leave it alone.
        echo "  skip   $target (not a symlink — remove it yourself if intended)"
      fi
      continue
    fi

    if [[ -L "$target" ]]; then
      current="$(readlink "$target")"
      if [[ "$current" == "$source_dir" ]]; then
        echo "  ok     $target (already linked)"
        continue
      fi
      echo "  relink $target"
      echo "           was: $current"
      run rm "$target"
    elif [[ -e "$target" ]]; then
      echo "  skip   $target (real directory, not a symlink — remove it first)"
      continue
    else
      echo "  link   $target"
    fi
    run ln -s "$source_dir" "$target"
  done
done

echo
if [[ $UNLINK -eq 1 ]]; then
  echo "Done. Checked ${#SKILLS[@]} skill(s) across $dirs_found directory/ies."
else
  echo "Done. Linked ${#SKILLS[@]} skill(s) into $dirs_found directory/ies — edits are live."
fi
