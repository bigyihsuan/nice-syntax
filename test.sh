#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR
shopt -s expand_aliases
source ~/.bash_aliases

./compile-grammar.sh $1

for l in $(cat $2); do
    echo "$l"
    echo "$l" | python3 $3
done
