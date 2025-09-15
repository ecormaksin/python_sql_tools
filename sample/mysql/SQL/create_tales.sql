-- Project Name : DBeaver Sample Database
-- Date/Time    : 2025/09/15 14:18:56
-- Author       : eight
-- RDBMS Type   : MySQL
-- Application  : A5:SQL Mk-2

-- invoice_line
DROP TABLE if exists invoice_line CASCADE;

CREATE TABLE invoice_line (
  invoice_line_id INT NOT NULL COMMENT 'invoice_line_id'
  , invoice_id BIGINT NOT NULL COMMENT 'invoice_id'
  , track_id BIGINT NOT NULL COMMENT 'track_id'
  , unit_price DECIMAL(9, 2) NOT NULL COMMENT 'unit_price'
  , quantity INT NOT NULL COMMENT 'quantity'
  , CONSTRAINT invoice_line_PKC PRIMARY KEY (invoice_line_id)
) COMMENT 'invoice_line' ;

CREATE INDEX invoice_line_IX1
  ON invoice_line(invoice_id);

CREATE INDEX invoice_line_IX2
  ON invoice_line(track_id);

-- playlist_track
DROP TABLE if exists playlist_track CASCADE;

CREATE TABLE playlist_track (
  play_list_id BIGINT NOT NULL COMMENT 'play_list_id'
  , track_id BIGINT NOT NULL COMMENT 'track_id'
  , CONSTRAINT playlist_track_PKC PRIMARY KEY (play_list_id,track_id)
) COMMENT 'playlist_track' ;

CREATE INDEX playlist_track_IX1
  ON playlist_track(track_id);

-- track
DROP TABLE if exists track CASCADE;

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

-- album
DROP TABLE if exists album CASCADE;

CREATE TABLE album (
  album_id BIGINT NOT NULL COMMENT 'album_id'
  , title VARCHAR(160) NOT NULL COMMENT 'title'
  , artist_id BIGINT NOT NULL COMMENT 'artist_id'
  , CONSTRAINT album_PKC PRIMARY KEY (album_id)
) COMMENT 'album' ;

CREATE INDEX album_IX1
  ON album(artist_id);

-- artist
DROP TABLE if exists artist CASCADE;

CREATE TABLE artist (
  artist_id BIGINT NOT NULL COMMENT 'artist_id'
  , name VARCHAR(120) NOT NULL COMMENT 'name'
  , CONSTRAINT artist_PKC PRIMARY KEY (artist_id)
) COMMENT 'artist' ;

-- genre
DROP TABLE if exists genre CASCADE;

CREATE TABLE genre (
  genre_id INT NOT NULL COMMENT 'genre_id'
  , name VARCHAR(255) NOT NULL COMMENT 'name'
  , CONSTRAINT genre_PKC PRIMARY KEY (genre_id)
) COMMENT 'genre' ;

-- invoice
DROP TABLE if exists invoice CASCADE;

CREATE TABLE invoice (
  invoice_id BIGINT NOT NULL COMMENT 'invoice_id'
  , customer_id BIGINT NOT NULL COMMENT 'customer_id'
  , invoice_date DATE NOT NULL COMMENT 'invoice_date'
  , billing_address VARCHAR(70) COMMENT 'billing_address'
  , billing_city VARCHAR(40) COMMENT 'billing_city'
  , billing_state VARCHAR(40) COMMENT 'billing_state'
  , billing_country VARCHAR(40) COMMENT 'billing_country'
  , billing_postal_code VARCHAR(10) COMMENT 'billing_postal_code'
  , total INT NOT NULL COMMENT 'total'
  , CONSTRAINT invoice_PKC PRIMARY KEY (invoice_id)
) COMMENT 'invoice' ;

CREATE INDEX invoice_IX1
  ON invoice(customer_id);

CREATE INDEX invoice_IX2
  ON invoice(invoice_date);

-- media_type
DROP TABLE if exists media_type CASCADE;

CREATE TABLE media_type (
  media_type_id INT NOT NULL COMMENT 'media_type_id'
  , name VARCHAR(30) NOT NULL COMMENT 'name'
  , CONSTRAINT media_type_PKC PRIMARY KEY (media_type_id)
) COMMENT 'media_type' ;

-- play_list
DROP TABLE if exists play_list CASCADE;

CREATE TABLE play_list (
  play_list_id BIGINT NOT NULL COMMENT 'play_list_id'
  , name VARCHAR(255) NOT NULL COMMENT 'name'
  , CONSTRAINT play_list_PKC PRIMARY KEY (play_list_id)
) COMMENT 'play_list' ;

-- customer
DROP TABLE if exists customer CASCADE;

CREATE TABLE customer (
  customer_id BIGINT NOT NULL COMMENT 'customer_id'
  , first_name VARCHAR(40) NOT NULL COMMENT 'first_name'
  , last_name VARCHAR(40) NOT NULL COMMENT 'last_name'
  , company VARCHAR(80) COMMENT 'company'
  , address VARCHAR(70) COMMENT 'address'
  , city VARCHAR(40) COMMENT 'city'
  , state VARCHAR(40) COMMENT 'state'
  , country VARCHAR(40) COMMENT 'country'
  , postal_code VARCHAR(10) COMMENT 'postal_code'
  , phone VARCHAR(24) COMMENT 'phone'
  , fax VARCHAR(24) COMMENT 'fax'
  , email VARCHAR(320) NOT NULL COMMENT 'email'
  , support_rep_id BIGINT COMMENT 'support_rep_id'
  , CONSTRAINT customer_PKC PRIMARY KEY (customer_id)
) COMMENT 'customer' ;

CREATE INDEX customer_IX1
  ON customer(first_name);

CREATE INDEX customer_IX2
  ON customer(last_name);

CREATE INDEX customer_IX3
  ON customer(email);

CREATE INDEX customer_IX4
  ON customer(support_rep_id);

-- employee
DROP TABLE if exists employee CASCADE;

CREATE TABLE employee (
  employee_id BIGINT NOT NULL COMMENT 'employee_id'
  , last_name VARCHAR(40) NOT NULL COMMENT 'last_name'
  , first_name VARCHAR(40) NOT NULL COMMENT 'first_name'
  , title VARCHAR(30) COMMENT 'title'
  , reports_to BIGINT COMMENT 'reports_to'
  , birth_date DATE COMMENT 'birth_date'
  , hire_date DATE COMMENT 'hire_date'
  , address VARCHAR(70) COMMENT 'address'
  , city VARCHAR(40) COMMENT 'city'
  , state VARCHAR(40) COMMENT 'state'
  , country VARCHAR(40) COMMENT 'country'
  , postal_code VARCHAR(10) COMMENT 'postal_code'
  , phone VARCHAR(24) COMMENT 'phone'
  , fax VARCHAR(24) COMMENT 'fax'
  , email VARCHAR(320) NOT NULL COMMENT 'email'
  , CONSTRAINT employee_PKC PRIMARY KEY (employee_id)
) COMMENT 'employee' ;

CREATE INDEX employee_IX1
  ON employee(last_name);

CREATE INDEX employee_IX2
  ON employee(first_name);

CREATE INDEX employee_IX3
  ON employee(email);

CREATE INDEX employee_IX4
  ON employee(reports_to);

ALTER TABLE album
  ADD CONSTRAINT album_FK1 FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE customer
  ADD CONSTRAINT customer_FK1 FOREIGN KEY (support_rep_id) REFERENCES employee(employee_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE employee
  ADD CONSTRAINT employee_FK1 FOREIGN KEY (reports_to) REFERENCES employee(employee_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE invoice
  ADD CONSTRAINT invoice_FK1 FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK1 FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK1 FOREIGN KEY (play_list_id) REFERENCES play_list(play_list_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE track
  ADD CONSTRAINT track_FK1 FOREIGN KEY (album_id) REFERENCES album(album_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE track
  ADD CONSTRAINT track_FK2 FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

ALTER TABLE track
  ADD CONSTRAINT track_FK3 FOREIGN KEY (media_type_id) REFERENCES media_type(media_type_id)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;

