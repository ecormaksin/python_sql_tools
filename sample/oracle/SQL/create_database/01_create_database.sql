-- use Docker container of container-registry.oracle.com/database/free:23.9.0.0-amd64
CREATE PLUGGABLE DATABASE dbeaver_sample 
  ADMIN USER dbeaver_sample IDENTIFIED BY password
    FILE_NAME_CONVERT = ('/opt/oracle/oradata/FREE/pdbseed/', 
                         '/opt/oracle/oradata/FREE/dbeaver_sample/');

ALTER PLUGGABLE DATABASE dbeaver_sample OPEN;

ALTER PLUGGABLE DATABASE dbeaver_sample SAVE STATE;
