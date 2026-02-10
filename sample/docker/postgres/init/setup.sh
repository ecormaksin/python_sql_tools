#!/usr/bin/env bash

export PGPASSWORD=secret

BASE_DIR=/setup

psql -U postgres -f ${BASE_DIR}/01.create_schemas.sql

TABLE_DDL_DIR=${BASE_DIR}/02.create_tables
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/01.artist.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/02.genre.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/03.media_type.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/04.album.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/05.play_list.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/06.employee.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/07.customer.sql
psql -U postgres -d postgres -f ${TABLE_DDL_DIR}/08.invoice.sql

VIEW_DDL_DIR=${BASE_DIR}/03.create_views
psql -U postgres -d postgres -f ${VIEW_DDL_DIR}/01.album.sql
