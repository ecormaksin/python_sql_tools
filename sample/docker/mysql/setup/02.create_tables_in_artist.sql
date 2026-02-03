-- artist
DROP TABLE if exists artist CASCADE;

CREATE TABLE artist (
  artist_id BIGINT NOT NULL COMMENT 'artist_id'
  , name VARCHAR(120) NOT NULL COMMENT 'name'
  , CONSTRAINT artist_PKC PRIMARY KEY (artist_id)
) COMMENT 'artist' ;

