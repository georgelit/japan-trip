#!/bin/sh
# Gives a friend write access to the page. Example: tools/invite.sh nadir-github-nick
[ -z "$1" ] && { echo "pass a GitHub username: tools/invite.sh USERNAME"; exit 1; }
gh api -X PUT "repos/georgelit/japan-trip/collaborators/$1" -f permission=push \
  && echo "✅ invitation sent to $1 — they confirm it by email or on github.com"
