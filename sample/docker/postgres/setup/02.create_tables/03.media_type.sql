CREATE TABLE media_type.media_type (
  media_type_id integer NOT NULL
  , name character varying(30) NOT NULL
  , CONSTRAINT media_type_PKC PRIMARY KEY (media_type_id)
) ;

COMMENT ON TABLE media_type.media_type IS 'media_type';
COMMENT ON COLUMN media_type.media_type.media_type_id IS 'media_type_id';
COMMENT ON COLUMN media_type.media_type.name IS 'name';
