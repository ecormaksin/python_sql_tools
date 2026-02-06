CREATE TABLE genre (
  genre_id INT NOT NULL COMMENT 'genre_id'
  , name VARCHAR(255) NOT NULL COMMENT 'name'
  , CONSTRAINT genre_PKC PRIMARY KEY (genre_id)
) COMMENT 'genre' ;

