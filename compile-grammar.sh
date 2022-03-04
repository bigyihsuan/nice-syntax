#!/usr/bin/env bash
# set -euo pipefail
# IFS=$'\n\t'
# trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR
shopt -s expand_aliases
source ~/.bash_aliases

antlr4 -Dlanguage=Python3 -visitor "$1"
