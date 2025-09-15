-- Project Name : DBeaver Sample Database
-- Date/Time    : 2025/09/15 14:32:41
-- Author       : eight
-- RDBMS Type   : Oracle Database
-- Application  : A5:SQL Mk-2

-- invoice_line
DROP TABLE invoice_line CASCADE CONSTRAINTS;

CREATE TABLE invoice_line (
  invoice_line_id NUMBER(10) NOT NULL
  , invoice_id NUMBER(19,0) NOT NULL
  , track_id NUMBER(19,0) NOT NULL
  , unit_price NUMBER(9, 2) NOT NULL
  , quantity NUMBER(10) NOT NULL
  , CONSTRAINT invoice_line_PKC PRIMARY KEY (invoice_line_id)
) ;

CREATE INDEX invoice_line_IX1
  ON invoice_line(invoice_id);

CREATE INDEX invoice_line_IX2
  ON invoice_line(track_id);

-- playlist_track
DROP TABLE playlist_track CASCADE CONSTRAINTS;

CREATE TABLE playlist_track (
  play_list_id NUMBER(19,0) NOT NULL
  , track_id NUMBER(19,0) NOT NULL
  , CONSTRAINT playlist_track_PKC PRIMARY KEY (play_list_id,track_id)
) ;

CREATE INDEX playlist_track_IX1
  ON playlist_track(track_id);

-- track
DROP TABLE track CASCADE CONSTRAINTS;

CREATE TABLE track (
  track_id NUMBER(19,0) NOT NULL
  , name NVARCHAR2(255) NOT NULL
  , album_id NUMBER(19,0)
  , media_type_id NUMBER(10) NOT NULL
  , genre_id NUMBER(10)
  , composer NVARCHAR2(255)
  , milliseconds NUMBER(10) NOT NULL
  , bytes NUMBER(10)
  , unit_price NUMBER(9, 2) NOT NULL
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
DROP TABLE album CASCADE CONSTRAINTS;

CREATE TABLE album (
  album_id NUMBER(19,0) NOT NULL
  , title NVARCHAR2(160) NOT NULL
  , artist_id NUMBER(19,0) NOT NULL
  , CONSTRAINT album_PKC PRIMARY KEY (album_id)
) ;

CREATE INDEX album_IX1
  ON album(artist_id);

-- artist
DROP TABLE artist CASCADE CONSTRAINTS;

CREATE TABLE artist (
  artist_id NUMBER(19,0) NOT NULL
  , name NVARCHAR2(120) NOT NULL
  , CONSTRAINT artist_PKC PRIMARY KEY (artist_id)
) ;

-- genre
DROP TABLE genre CASCADE CONSTRAINTS;

CREATE TABLE genre (
  genre_id NUMBER(10) NOT NULL
  , name NVARCHAR2(255) NOT NULL
  , CONSTRAINT genre_PKC PRIMARY KEY (genre_id)
) ;

-- invoice
DROP TABLE invoice CASCADE CONSTRAINTS;

CREATE TABLE invoice (
  invoice_id NUMBER(19,0) NOT NULL
  , customer_id NUMBER(19,0) NOT NULL
  , invoice_date DATE NOT NULL
  , billing_address NVARCHAR2(70)
  , billing_city NVARCHAR2(40)
  , billing_state NVARCHAR2(40)
  , billing_country NVARCHAR2(40)
  , billing_postal_code NVARCHAR2(10)
  , total NUMBER(10) NOT NULL
  , CONSTRAINT invoice_PKC PRIMARY KEY (invoice_id)
) ;

CREATE INDEX invoice_IX1
  ON invoice(customer_id);

CREATE INDEX invoice_IX2
  ON invoice(invoice_date);

-- media_type
DROP TABLE media_type CASCADE CONSTRAINTS;

CREATE TABLE media_type (
  media_type_id NUMBER(10) NOT NULL
  , name NVARCHAR2(30) NOT NULL
  , CONSTRAINT media_type_PKC PRIMARY KEY (media_type_id)
) ;

-- play_list
DROP TABLE play_list CASCADE CONSTRAINTS;

CREATE TABLE play_list (
  play_list_id NUMBER(19,0) NOT NULL
  , name NVARCHAR2(255) NOT NULL
  , CONSTRAINT play_list_PKC PRIMARY KEY (play_list_id)
) ;

-- customer
DROP TABLE customer CASCADE CONSTRAINTS;

CREATE TABLE customer (
  customer_id NUMBER(19,0) NOT NULL
  , first_name NVARCHAR2(40) NOT NULL
  , last_name NVARCHAR2(40) NOT NULL
  , company NVARCHAR2(80)
  , address NVARCHAR2(70)
  , city NVARCHAR2(40)
  , state NVARCHAR2(40)
  , country NVARCHAR2(40)
  , postal_code NVARCHAR2(10)
  , phone NVARCHAR2(24)
  , fax NVARCHAR2(24)
  , email NVARCHAR2(320) NOT NULL
  , support_rep_id NUMBER(19,0)
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
DROP TABLE employee CASCADE CONSTRAINTS;

CREATE TABLE employee (
  employee_id NUMBER(19,0) NOT NULL
  , last_name NVARCHAR2(40) NOT NULL
  , first_name NVARCHAR2(40) NOT NULL
  , title NVARCHAR2(30)
  , reports_to NUMBER(19,0)
  , birth_date DATE
  , hire_date DATE
  , address NVARCHAR2(70)
  , city NVARCHAR2(40)
  , state NVARCHAR2(40)
  , country NVARCHAR2(40)
  , postal_code NVARCHAR2(10)
  , phone NVARCHAR2(24)
  , fax NVARCHAR2(24)
  , email NVARCHAR2(320) NOT NULL
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
  ADD CONSTRAINT album_FK1 FOREIGN KEY (artist_id) REFERENCES artist(artist_id);

ALTER TABLE customer
  ADD CONSTRAINT customer_FK1 FOREIGN KEY (support_rep_id) REFERENCES employee(employee_id);

ALTER TABLE employee
  ADD CONSTRAINT employee_FK1 FOREIGN KEY (reports_to) REFERENCES employee(employee_id);

ALTER TABLE invoice
  ADD CONSTRAINT invoice_FK1 FOREIGN KEY (customer_id) REFERENCES customer(customer_id);

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK1 FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id);

ALTER TABLE invoice_line
  ADD CONSTRAINT invoice_line_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id);

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK1 FOREIGN KEY (play_list_id) REFERENCES play_list(play_list_id);

ALTER TABLE playlist_track
  ADD CONSTRAINT playlist_track_FK2 FOREIGN KEY (track_id) REFERENCES track(track_id);

ALTER TABLE track
  ADD CONSTRAINT track_FK1 FOREIGN KEY (album_id) REFERENCES album(album_id);

ALTER TABLE track
  ADD CONSTRAINT track_FK2 FOREIGN KEY (genre_id) REFERENCES genre(genre_id);

ALTER TABLE track
  ADD CONSTRAINT track_FK3 FOREIGN KEY (media_type_id) REFERENCES media_type(media_type_id);

COMMENT ON TABLE invoice_line IS 'invoice_line';
COMMENT ON COLUMN invoice_line.invoice_line_id IS 'invoice_line_id';
COMMENT ON COLUMN invoice_line.invoice_id IS 'invoice_id';
COMMENT ON COLUMN invoice_line.track_id IS 'track_id';
COMMENT ON COLUMN invoice_line.unit_price IS 'unit_price';
COMMENT ON COLUMN invoice_line.quantity IS 'quantity';

COMMENT ON TABLE playlist_track IS 'playlist_track';
COMMENT ON COLUMN playlist_track.play_list_id IS 'play_list_id';
COMMENT ON COLUMN playlist_track.track_id IS 'track_id';

COMMENT ON TABLE track IS 'track';
COMMENT ON COLUMN track.track_id IS 'track_id';
COMMENT ON COLUMN track.name IS 'name';
COMMENT ON COLUMN track.album_id IS 'album_id';
COMMENT ON COLUMN track.media_type_id IS 'media_type_id';
COMMENT ON COLUMN track.genre_id IS 'genre_id';
COMMENT ON COLUMN track.composer IS 'composer';
COMMENT ON COLUMN track.milliseconds IS 'milliseconds';
COMMENT ON COLUMN track.bytes IS 'bytes';
COMMENT ON COLUMN track.unit_price IS 'unit_price';

COMMENT ON TABLE album IS 'album';
COMMENT ON COLUMN album.album_id IS 'album_id';
COMMENT ON COLUMN album.title IS 'title';
COMMENT ON COLUMN album.artist_id IS 'artist_id';

COMMENT ON TABLE artist IS 'artist';
COMMENT ON COLUMN artist.artist_id IS 'artist_id';
COMMENT ON COLUMN artist.name IS 'name';

COMMENT ON TABLE genre IS 'genre';
COMMENT ON COLUMN genre.genre_id IS 'genre_id';
COMMENT ON COLUMN genre.name IS 'name';

COMMENT ON TABLE invoice IS 'invoice';
COMMENT ON COLUMN invoice.invoice_id IS 'invoice_id';
COMMENT ON COLUMN invoice.customer_id IS 'customer_id';
COMMENT ON COLUMN invoice.invoice_date IS 'invoice_date';
COMMENT ON COLUMN invoice.billing_address IS 'billing_address';
COMMENT ON COLUMN invoice.billing_city IS 'billing_city';
COMMENT ON COLUMN invoice.billing_state IS 'billing_state';
COMMENT ON COLUMN invoice.billing_country IS 'billing_country';
COMMENT ON COLUMN invoice.billing_postal_code IS 'billing_postal_code';
COMMENT ON COLUMN invoice.total IS 'total';

COMMENT ON TABLE media_type IS 'media_type';
COMMENT ON COLUMN media_type.media_type_id IS 'media_type_id';
COMMENT ON COLUMN media_type.name IS 'name';

COMMENT ON TABLE play_list IS 'play_list';
COMMENT ON COLUMN play_list.play_list_id IS 'play_list_id';
COMMENT ON COLUMN play_list.name IS 'name';

COMMENT ON TABLE customer IS 'customer';
COMMENT ON COLUMN customer.customer_id IS 'customer_id';
COMMENT ON COLUMN customer.first_name IS 'first_name';
COMMENT ON COLUMN customer.last_name IS 'last_name';
COMMENT ON COLUMN customer.company IS 'company';
COMMENT ON COLUMN customer.address IS 'address';
COMMENT ON COLUMN customer.city IS 'city';
COMMENT ON COLUMN customer.state IS 'state';
COMMENT ON COLUMN customer.country IS 'country';
COMMENT ON COLUMN customer.postal_code IS 'postal_code';
COMMENT ON COLUMN customer.phone IS 'phone';
COMMENT ON COLUMN customer.fax IS 'fax';
COMMENT ON COLUMN customer.email IS 'email';
COMMENT ON COLUMN customer.support_rep_id IS 'support_rep_id';

COMMENT ON TABLE employee IS 'employee';
COMMENT ON COLUMN employee.employee_id IS 'employee_id';
COMMENT ON COLUMN employee.last_name IS 'last_name';
COMMENT ON COLUMN employee.first_name IS 'first_name';
COMMENT ON COLUMN employee.title IS 'title';
COMMENT ON COLUMN employee.reports_to IS 'reports_to';
COMMENT ON COLUMN employee.birth_date IS 'birth_date';
COMMENT ON COLUMN employee.hire_date IS 'hire_date';
COMMENT ON COLUMN employee.address IS 'address';
COMMENT ON COLUMN employee.city IS 'city';
COMMENT ON COLUMN employee.state IS 'state';
COMMENT ON COLUMN employee.country IS 'country';
COMMENT ON COLUMN employee.postal_code IS 'postal_code';
COMMENT ON COLUMN employee.phone IS 'phone';
COMMENT ON COLUMN employee.fax IS 'fax';
COMMENT ON COLUMN employee.email IS 'email';

