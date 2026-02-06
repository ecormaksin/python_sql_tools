CREATE TABLE media_type (
  media_type_id INT NOT NULL COMMENT 'media_type_id'
  , name VARCHAR(30) NOT NULL COMMENT 'name'
  , CONSTRAINT media_type_PKC PRIMARY KEY (media_type_id)
) COMMENT 'media_type' ;

