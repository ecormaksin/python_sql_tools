-- Project Name : DBeaver Sample Database
-- Date/Time    : 2025/09/15 14:27:26
-- Author       : eight
-- RDBMS Type   : Microsoft SQL Server 2016 ～
-- Application  : A5:SQL Mk-2

-- invoice_line
DROP TABLE if exists invoice_line;

CREATE TABLE invoice_line (
  invoice_line_id INTEGER NOT NULL
  , invoice_id BIGINT NOT NULL
  , track_id BIGINT NOT NULL
  , unit_price DECIMAL(9, 2) NOT NULL
  , quantity INTEGER NOT NULL
  , CONSTRAINT invoice_line_PKC PRIMARY KEY (invoice_line_id)
) ;

CREATE INDEX invoice_line_IX1
  ON invoice_line(invoice_id);

CREATE INDEX invoice_line_IX2
  ON invoice_line(track_id);

-- playlist_track
DROP TABLE if exists playlist_track;

CREATE TABLE playlist_track (
  play_list_id BIGINT NOT NULL
  , track_id BIGINT NOT NULL
  , CONSTRAINT playlist_track_PKC PRIMARY KEY (play_list_id,track_id)
) ;

CREATE INDEX playlist_track_IX1
  ON playlist_track(track_id);

-- track
DROP TABLE if exists track;

CREATE TABLE track (
  track_id BIGINT NOT NULL
  , name NVARCHAR(255) NOT NULL
  , album_id BIGINT
  , media_type_id INTEGER NOT NULL
  , genre_id INTEGER
  , composer NVARCHAR(255)
  , milliseconds INTEGER NOT NULL
  , bytes INTEGER
  , unit_price DECIMAL(9, 2) NOT NULL
  , CONSTRAINT track_PKC PRIMARY KEY (track_id)
) ;

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
DROP TABLE if exists album;

CREATE TABLE album (
  album_id BIGINT NOT NULL
  , title NVARCHAR(160) NOT NULL
  , artist_id BIGINT NOT NULL
  , CONSTRAINT album_PKC PRIMARY KEY (album_id)
) ;

CREATE INDEX album_IX1
  ON album(artist_id);

-- artist
DROP TABLE if exists artist;

CREATE TABLE artist (
  artist_id BIGINT NOT NULL
  , name NVARCHAR(120) NOT NULL
  , CONSTRAINT artist_PKC PRIMARY KEY (artist_id)
) ;

-- genre
DROP TABLE if exists genre;

CREATE TABLE genre (
  genre_id INTEGER NOT NULL
  , name NVARCHAR(255) NOT NULL
  , CONSTRAINT genre_PKC PRIMARY KEY (genre_id)
) ;

-- invoice
DROP TABLE if exists invoice;

CREATE TABLE invoice (
  invoice_id BIGINT NOT NULL
  , customer_id BIGINT NOT NULL
  , invoice_date DATE NOT NULL
  , billing_address NVARCHAR(70)
  , billing_city NVARCHAR(40)
  , billing_state NVARCHAR(40)
  , billing_country NVARCHAR(40)
  , billing_postal_code NVARCHAR(10)
  , total INTEGER NOT NULL
  , CONSTRAINT invoice_PKC PRIMARY KEY (invoice_id)
) ;

CREATE INDEX invoice_IX1
  ON invoice(customer_id);

CREATE INDEX invoice_IX2
  ON invoice(invoice_date);

-- media_type
DROP TABLE if exists media_type;

CREATE TABLE media_type (
  media_type_id INTEGER NOT NULL
  , name NVARCHAR(30) NOT NULL
  , CONSTRAINT media_type_PKC PRIMARY KEY (media_type_id)
) ;

-- play_list
DROP TABLE if exists play_list;

CREATE TABLE play_list (
  play_list_id BIGINT NOT NULL
  , name NVARCHAR(255) NOT NULL
  , CONSTRAINT play_list_PKC PRIMARY KEY (play_list_id)
) ;

-- customer
DROP TABLE if exists customer;

CREATE TABLE customer (
  customer_id BIGINT NOT NULL
  , first_name NVARCHAR(40) NOT NULL
  , last_name NVARCHAR(40) NOT NULL
  , company NVARCHAR(80)
  , address NVARCHAR(70)
  , city NVARCHAR(40)
  , state NVARCHAR(40)
  , country NVARCHAR(40)
  , postal_code NVARCHAR(10)
  , phone NVARCHAR(24)
  , fax NVARCHAR(24)
  , email NVARCHAR(320) NOT NULL
  , support_rep_id BIGINT
  , CONSTRAINT customer_PKC PRIMARY KEY (customer_id)
) ;

CREATE INDEX customer_IX1
  ON customer(first_name);

CREATE INDEX customer_IX2
  ON customer(last_name);

CREATE INDEX customer_IX3
  ON customer(email);

CREATE INDEX customer_IX4
  ON customer(support_rep_id);

-- employee
DROP TABLE if exists employee;

CREATE TABLE employee (
  employee_id BIGINT NOT NULL
  , last_name NVARCHAR(40) NOT NULL
  , first_name NVARCHAR(40) NOT NULL
  , title NVARCHAR(30)
  , reports_to BIGINT
  , birth_date DATE
  , hire_date DATE
  , address NVARCHAR(70)
  , city NVARCHAR(40)
  , state NVARCHAR(40)
  , country NVARCHAR(40)
  , postal_code NVARCHAR(10)
  , phone NVARCHAR(24)
  , fax NVARCHAR(24)
  , email NVARCHAR(320) NOT NULL
  , CONSTRAINT employee_PKC PRIMARY KEY (employee_id)
) ;

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
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE customer
  ADD CONSTRAINT customer_FK1 FOREIGN KEY (support_rep_id) REFERENCES employee(employee_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE employee
  ADD CONSTRAINT employee_FK1 FOREIGN KEY (reports_to) REFERENCES employee(employee_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE invoice
  ADD CONSTRAINT invoice_FK1 FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK1 FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK1 FOREIGN KEY (play_list_id) REFERENCES play_list(play_list_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE track
  ADD CONSTRAINT track_FK1 FOREIGN KEY (album_id) REFERENCES album(album_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE track
  ADD CONSTRAINT track_FK2 FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE track
  ADD CONSTRAINT track_FK3 FOREIGN KEY (media_type_id) REFERENCES media_type(media_type_id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

EXECUTE sp_addextendedproperty N'MS_Description', N'invoice_line', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'invoice_line_id', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', N'COLUMN', N'invoice_line_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'invoice_id', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', N'COLUMN', N'invoice_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'track_id', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', N'COLUMN', N'track_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'unit_price', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', N'COLUMN', N'unit_price';
EXECUTE sp_addextendedproperty N'MS_Description', N'quantity', N'SCHEMA', N'dbo', N'TABLE', N'invoice_line', N'COLUMN', N'quantity';

EXECUTE sp_addextendedproperty N'MS_Description', N'invoice', N'SCHEMA', N'dbo', N'TABLE', N'invoice', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'invoice_id', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'invoice_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'customer_id', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'customer_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'invoice_date', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'invoice_date';
EXECUTE sp_addextendedproperty N'MS_Description', N'billing_address', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'billing_address';
EXECUTE sp_addextendedproperty N'MS_Description', N'billing_city', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'billing_city';
EXECUTE sp_addextendedproperty N'MS_Description', N'billing_state', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'billing_state';
EXECUTE sp_addextendedproperty N'MS_Description', N'billing_country', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'billing_country';
EXECUTE sp_addextendedproperty N'MS_Description', N'billing_postal_code', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'billing_postal_code';
EXECUTE sp_addextendedproperty N'MS_Description', N'total', N'SCHEMA', N'dbo', N'TABLE', N'invoice', N'COLUMN', N'total';

EXECUTE sp_addextendedproperty N'MS_Description', N'employee', N'SCHEMA', N'dbo', N'TABLE', N'employee', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'employee_id', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'employee_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'last_name', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'last_name';
EXECUTE sp_addextendedproperty N'MS_Description', N'first_name', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'first_name';
EXECUTE sp_addextendedproperty N'MS_Description', N'title', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'title';
EXECUTE sp_addextendedproperty N'MS_Description', N'reports_to', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'reports_to';
EXECUTE sp_addextendedproperty N'MS_Description', N'birth_date', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'birth_date';
EXECUTE sp_addextendedproperty N'MS_Description', N'hire_date', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'hire_date';
EXECUTE sp_addextendedproperty N'MS_Description', N'address', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'address';
EXECUTE sp_addextendedproperty N'MS_Description', N'city', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'city';
EXECUTE sp_addextendedproperty N'MS_Description', N'state', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'state';
EXECUTE sp_addextendedproperty N'MS_Description', N'country', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'country';
EXECUTE sp_addextendedproperty N'MS_Description', N'postal_code', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'postal_code';
EXECUTE sp_addextendedproperty N'MS_Description', N'phone', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'phone';
EXECUTE sp_addextendedproperty N'MS_Description', N'fax', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'fax';
EXECUTE sp_addextendedproperty N'MS_Description', N'email', N'SCHEMA', N'dbo', N'TABLE', N'employee', N'COLUMN', N'email';

EXECUTE sp_addextendedproperty N'MS_Description', N'customer', N'SCHEMA', N'dbo', N'TABLE', N'customer', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'customer_id', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'customer_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'first_name', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'first_name';
EXECUTE sp_addextendedproperty N'MS_Description', N'last_name', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'last_name';
EXECUTE sp_addextendedproperty N'MS_Description', N'company', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'company';
EXECUTE sp_addextendedproperty N'MS_Description', N'address', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'address';
EXECUTE sp_addextendedproperty N'MS_Description', N'city', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'city';
EXECUTE sp_addextendedproperty N'MS_Description', N'state', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'state';
EXECUTE sp_addextendedproperty N'MS_Description', N'country', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'country';
EXECUTE sp_addextendedproperty N'MS_Description', N'postal_code', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'postal_code';
EXECUTE sp_addextendedproperty N'MS_Description', N'phone', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'phone';
EXECUTE sp_addextendedproperty N'MS_Description', N'fax', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'fax';
EXECUTE sp_addextendedproperty N'MS_Description', N'email', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'email';
EXECUTE sp_addextendedproperty N'MS_Description', N'support_rep_id', N'SCHEMA', N'dbo', N'TABLE', N'customer', N'COLUMN', N'support_rep_id';

EXECUTE sp_addextendedproperty N'MS_Description', N'playlist_track', N'SCHEMA', N'dbo', N'TABLE', N'playlist_track', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'play_list_id', N'SCHEMA', N'dbo', N'TABLE', N'playlist_track', N'COLUMN', N'play_list_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'track_id', N'SCHEMA', N'dbo', N'TABLE', N'playlist_track', N'COLUMN', N'track_id';

EXECUTE sp_addextendedproperty N'MS_Description', N'play_list', N'SCHEMA', N'dbo', N'TABLE', N'play_list', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'play_list_id', N'SCHEMA', N'dbo', N'TABLE', N'play_list', N'COLUMN', N'play_list_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'name', N'SCHEMA', N'dbo', N'TABLE', N'play_list', N'COLUMN', N'name';

EXECUTE sp_addextendedproperty N'MS_Description', N'track', N'SCHEMA', N'dbo', N'TABLE', N'track', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'track_id', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'track_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'name', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'name';
EXECUTE sp_addextendedproperty N'MS_Description', N'album_id', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'album_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'media_type_id', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'media_type_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'genre_id', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'genre_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'composer', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'composer';
EXECUTE sp_addextendedproperty N'MS_Description', N'milliseconds', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'milliseconds';
EXECUTE sp_addextendedproperty N'MS_Description', N'bytes', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'bytes';
EXECUTE sp_addextendedproperty N'MS_Description', N'unit_price', N'SCHEMA', N'dbo', N'TABLE', N'track', N'COLUMN', N'unit_price';

EXECUTE sp_addextendedproperty N'MS_Description', N'media_type', N'SCHEMA', N'dbo', N'TABLE', N'media_type', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'media_type_id', N'SCHEMA', N'dbo', N'TABLE', N'media_type', N'COLUMN', N'media_type_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'name', N'SCHEMA', N'dbo', N'TABLE', N'media_type', N'COLUMN', N'name';

EXECUTE sp_addextendedproperty N'MS_Description', N'genre', N'SCHEMA', N'dbo', N'TABLE', N'genre', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'genre_id', N'SCHEMA', N'dbo', N'TABLE', N'genre', N'COLUMN', N'genre_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'name', N'SCHEMA', N'dbo', N'TABLE', N'genre', N'COLUMN', N'name';

EXECUTE sp_addextendedproperty N'MS_Description', N'album', N'SCHEMA', N'dbo', N'TABLE', N'album', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'album_id', N'SCHEMA', N'dbo', N'TABLE', N'album', N'COLUMN', N'album_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'title', N'SCHEMA', N'dbo', N'TABLE', N'album', N'COLUMN', N'title';
EXECUTE sp_addextendedproperty N'MS_Description', N'artist_id', N'SCHEMA', N'dbo', N'TABLE', N'album', N'COLUMN', N'artist_id';

EXECUTE sp_addextendedproperty N'MS_Description', N'artist', N'SCHEMA', N'dbo', N'TABLE', N'artist', NULL, NULL;
EXECUTE sp_addextendedproperty N'MS_Description', N'artist_id', N'SCHEMA', N'dbo', N'TABLE', N'artist', N'COLUMN', N'artist_id';
EXECUTE sp_addextendedproperty N'MS_Description', N'name', N'SCHEMA', N'dbo', N'TABLE', N'artist', N'COLUMN', N'name';

