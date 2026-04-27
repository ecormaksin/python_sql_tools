#!/usr/bin/env bash

declare -a databases=("artist" "genre" "media_type" "album" "play_list" "employee" "customer" "invoice")

i=1
for database in "${databases[@]}"; do
  num=$(printf "%02d" "$i")
  file_name="${num}.$database.sql"
  echo $file_name
  i=$((i + 1))
done
