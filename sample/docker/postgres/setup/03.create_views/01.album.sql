CREATE OR REPLACE VIEW album.album_view AS 
select 
  tbl_1.artist_id,
  tbl_1.name as artist_name,
  tbl_2.album_id,
  tbl_2.title as album_title
from
  artist.artist tbl_1
  inner join album.album tbl_2
    on 
    tbl_2.artist_id = tbl_1.artist_id
;

CREATE OR REPLACE VIEW album.track_view AS 
select 
  tbl_1.artist_id,
  tbl_1.artist_name,
  tbl_1.album_id,
  tbl_1.album_title,
  tbl_2.track_id,
  tbl_2.name as track_name,
  tbl_2.media_type_id,
  tbl_3.name as media_type_name,
  tbl_2.genre_id,
  tbl_4.name as genre_name,
  tbl_2.composer,
  tbl_2.milliseconds,
  tbl_2.bytes,
  tbl_2.unit_price
from
  album.album_view tbl_1
  inner join album.track tbl_2
    on 
    tbl_2.album_id = tbl_1.album_id
  inner join media_type.media_type tbl_3
    on 
    tbl_3.media_type_id = tbl_2.media_type_id
  inner join genre.genre tbl_4
    on
    tbl_4.genre_id = tbl_2.genre_id
;

