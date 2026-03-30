CREATE TABLE album.album (
  album_id BIGINT NOT NULL
  , title character varying(160) NOT NULL
  , artist_id BIGINT NOT NULL
  , CONSTRAINT album_PKC PRIMARY KEY (album_id)
  , CONSTRAINT album_FK1 FOREIGN KEY (artist_id)
    REFERENCES artist.artist (artist_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ;

CREATE INDEX album_IX1
  ON album.album(artist_id);

COMMENT ON TABLE album.album IS 'album';
COMMENT ON COLUMN album.album.album_id IS 'album_id';
COMMENT ON COLUMN album.album.title IS 'title';
COMMENT ON COLUMN album.album.artist_id IS 'artist_id';

CREATE TABLE album.track (
  track_id BIGINT NOT NULL
  , name character varying(255) NOT NULL
  , album_id BIGINT
  , media_type_id integer NOT NULL
  , genre_id integer
  , composer character varying(255)
  , milliseconds integer NOT NULL
  , bytes integer
  , unit_price numeric(9, 2) NOT NULL
  , CONSTRAINT track_PKC PRIMARY KEY (track_id)
  , CONSTRAINT track_FK1 FOREIGN KEY (album_id)
    REFERENCES album.album (album_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
  , CONSTRAINT track_FK2 FOREIGN KEY (media_type_id)
    REFERENCES media_type.media_type (media_type_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
  , CONSTRAINT track_FK3 FOREIGN KEY (genre_id)
    REFERENCES genre.genre (genre_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ;

CREATE INDEX track_IX1
  ON album.track(name);

CREATE INDEX track_IX2
  ON album.track(album_id);

CREATE INDEX track_IX3
  ON album.track(genre_id);

CREATE INDEX track_IX4
  ON album.track(media_type_id);

CREATE INDEX track_IX5
  ON album.track(composer);

COMMENT ON TABLE album.track IS 'track';
COMMENT ON COLUMN album.track.track_id IS 'track_id';
COMMENT ON COLUMN album.track.name IS 'name';
COMMENT ON COLUMN album.track.album_id IS 'album_id';
COMMENT ON COLUMN album.track.media_type_id IS 'media_type_id';
COMMENT ON COLUMN album.track.genre_id IS 'genre_id';
COMMENT ON COLUMN album.track.composer IS 'composer';
COMMENT ON COLUMN album.track.milliseconds IS 'milliseconds';
COMMENT ON COLUMN album.track.bytes IS 'bytes';
COMMENT ON COLUMN album.track.unit_price IS 'unit_price';
