CREATE TABLE artist.artist (
  artist_id BIGINT NOT NULL
  , name character varying(120) NOT NULL
  , CONSTRAINT artist_PKC PRIMARY KEY (artist_id)
) ;

COMMENT ON TABLE artist.artist IS 'artist';
COMMENT ON COLUMN artist.artist.artist_id IS 'artist_id';
COMMENT ON COLUMN artist.artist.name IS 'name';
