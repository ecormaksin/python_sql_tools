CREATE TABLE play_list.play_list (
  play_list_id BIGINT NOT NULL
  , name character varying(255) NOT NULL
  , CONSTRAINT play_list_PKC PRIMARY KEY (play_list_id)
) ;

COMMENT ON TABLE play_list.play_list IS 'play_list';
COMMENT ON COLUMN play_list.play_list.play_list_id IS 'play_list_id';
COMMENT ON COLUMN play_list.play_list.name IS 'name';

CREATE TABLE play_list.playlist_track (
  play_list_id BIGINT NOT NULL
  , track_id BIGINT NOT NULL
  , CONSTRAINT playlist_track_PKC PRIMARY KEY (play_list_id,track_id)
  , CONSTRAINT playlist_track_FK1 FOREIGN KEY (play_list_id)
    REFERENCES play_list.play_list (play_list_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
  , CONSTRAINT playlist_track_FK2 FOREIGN KEY (track_id)
    REFERENCES album.track (track_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ;

CREATE INDEX playlist_track_IX1
  ON play_list.playlist_track(track_id);

COMMENT ON TABLE play_list.playlist_track IS 'playlist_track';
COMMENT ON COLUMN play_list.playlist_track.play_list_id IS 'play_list_id';
COMMENT ON COLUMN play_list.playlist_track.track_id IS 'track_id';
