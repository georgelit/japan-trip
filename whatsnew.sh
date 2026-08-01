#!/bin/sh
# What changed, and who changed it. Reads the real git history, never guesses.
#   ./whatsnew.sh              every version, newest first
#   ./whatsnew.sh --by nadir   only Nadir's versions
#   ./whatsnew.sh --since 5    everything after v5
#   ./whatsnew.sh --diff 5     exactly what v5 changed
exec python3 "$(dirname "$0")/tools/whatsnew.py" "$@"
