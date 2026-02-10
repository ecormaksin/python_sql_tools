CREATE TABLE genre.genre (
  genre_id integer NOT NULL
  , name character varying(255) NOT NULL
  , CONSTRAINT genre_PKC PRIMARY KEY (genre_id)
) ;

COMMENT ON TABLE genre.genre IS 'genre';
COMMENT ON COLUMN genre.genre.genre_id IS 'genre_id';
COMMENT ON COLUMN genre.genre.name IS 'name';