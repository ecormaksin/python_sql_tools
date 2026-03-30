CREATE TABLE album (
  album_id BIGINT NOT NULL COMMENT 'album_id'
  , title VARCHAR(160) NOT NULL COMMENT 'title'
  , artist_id BIGINT NOT NULL COMMENT 'artist_id'
  , CONSTRAINT album_PKC PRIMARY KEY (album_id)
  , CONSTRAINT album_FK1 FOREIGN KEY (artist_id)
    REFERENCES artist.artist (artist_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) COMMENT 'album' ;

CREATE INDEX album_IX1
  ON album(artist_id);

CREATE TABLE track (
  track_id BIGINT NOT NULL COMMENT 'track_id'
  , name VARCHAR(255) NOT NULL COMMENT 'name'
  , album_id BIGINT COMMENT 'album_id'
  , media_type_id INT NOT NULL COMMENT 'media_type_id'
  , genre_id INT COMMENT 'genre_id'
  , composer VARCHAR(255) COMMENT 'composer'
  , milliseconds INT NOT NULL COMMENT 'milliseconds'
  , bytes INT COMMENT 'bytes'
  , unit_price DECIMAL(9, 2) NOT NULL COMMENT 'unit_price'
  , CONSTRAINT track_PKC PRIMARY KEY (track_id)
  , CONSTRAINT track_FK1 FOREIGN KEY (album_id)
    REFERENCES album (album_id)
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
) COMMENT 'track' ;

CREATE INDEX track_IX1
  ON track(name);

CREATE INDEX track_IX2
  ON track(album_id);

CREATE INDEX track_IX3
  ON track(genre_id);

CREATE INDEX track_IX4
  ON track(media_type_id);

CREATE INDEX track_IX5
  ON track(composer);
