#!/usr/bin/env bash

export PGPASSWORD=secret

BASE_DIR=/setup


declare -a databases=("artist" "genre" "media_type" "album" "play_list" "employee" "customer" "invoice")

SCHEMA_DDL_DIR=${BASE_DIR}/01.create_databases
i=1
for database in "${databases[@]}"; do
  num=$(printf "%02d" "$i")
  file_name="${num}.$database.sql"

  psql -U postgres -f "${SCHEMA_DDL_DIR}"/"${file_name}"

  i=$((i + 1))
done

TABLE_DDL_DIR=${BASE_DIR}/02.create_tables
i=1
for database in "${databases[@]}"; do
  num=$(printf "%02d" "$i")
  file_name="${num}.$database.sql"

  mysql --defaults-extra-file="${CONF_FILE_PATH}" --database="${database}" < "${TABLE_DDL_DIR}"/"${file_name}"
  psql -U postgres -d postgres -f "${TABLE_DDL_DIR}"/"${file_name}"

  i=$((i + 1))
done

VIEW_DDL_DIR=${BASE_DIR}/03.create_views
psql -U postgres -d postgres -f ${VIEW_DDL_DIR}/01.album.sql
