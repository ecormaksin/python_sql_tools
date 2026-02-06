#!/usr/bin/env bash

BASE_DIR=/setup
CONF_FILE_PATH=${BASE_DIR}/my.cnf

mysql --defaults-extra-file=${CONF_FILE_PATH} < ${BASE_DIR}/01.create_databases.sql

TABLE_DDL_DIR=${BASE_DIR}/02.create_tables
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=artist < ${TABLE_DDL_DIR}/01.artist.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=genre < ${TABLE_DDL_DIR}/02.genre.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=media_type < ${TABLE_DDL_DIR}/03.media_type.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=album < ${TABLE_DDL_DIR}/04.album.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=play_list < ${TABLE_DDL_DIR}/05.play_list.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=employee < ${TABLE_DDL_DIR}/06.employee.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=customer < ${TABLE_DDL_DIR}/07.customer.sql
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=invoice < ${TABLE_DDL_DIR}/08.invoice.sql

VIEW_DDL_DIR=${BASE_DIR}/03.create_views
mysql --defaults-extra-file=${CONF_FILE_PATH} --database=album < ${VIEW_DDL_DIR}/01.album.sql
