#!/usr/bin/env sh

if ! which ezjail-admin > /dev/null 2>&1; then
  echo "Please install ezjail-admin first"
  echo "pkg install ezjail"
  exit 1
fi

ezjail-admin list | awk 'BEGIN { ORS=""; print "{" } NR>=3 {
  printf "%s\"%s\" : [ \"%s\" ]", separator, $4, $3
  separator = ", "
} END { print "}" }'

