#!/bin/sh
# Publishes the Japan trip page. Example: ./publish.sh "moved Shirakawa-go to day 8"
exec python3 "$(dirname "$0")/tools/publish.py" "$@"
