CREATE TABLE play_list (
  play_list_id BIGINT NOT NULL COMMENT 'play_list_id'
  , name VARCHAR(255) NOT NULL COMMENT 'name'
  , CONSTRAINT play_list_PKC PRIMARY KEY (play_list_id)
) COMMENT 'play_list' ;

CREATE TABLE playlist_track (
  play_list_id BIGINT NOT NULL COMMENT 'play_list_id'
  , track_id BIGINT NOT NULL COMMENT 'track_id'
  , CONSTRAINT playlist_track_PKC PRIMARY KEY (play_list_id,track_id)
  , CONSTRAINT playlist_track_FK1 FOREIGN KEY (play_list_id)
    REFERENCES play_list (play_list_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
  , CONSTRAINT playlist_track_FK2 FOREIGN KEY (track_id)
    REFERENCES album.track (track_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) COMMENT 'playlist_track' ;

CREATE INDEX playlist_track_IX1
  ON playlist_track(track_id);
