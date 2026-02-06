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
  , CONSTRAINT invoice_FK1 FOREIGN KEY (customer_id)
    REFERENCES customer.customer (customer_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) COMMENT 'invoice' ;

CREATE INDEX invoice_IX1
  ON invoice(customer_id);

CREATE INDEX invoice_IX2
  ON invoice(invoice_date);

CREATE TABLE invoice_line (
  invoice_line_id INT NOT NULL COMMENT 'invoice_line_id'
  , invoice_id BIGINT NOT NULL COMMENT 'invoice_id'
  , track_id BIGINT NOT NULL COMMENT 'track_id'
  , unit_price DECIMAL(9, 2) NOT NULL COMMENT 'unit_price'
  , quantity INT NOT NULL COMMENT 'quantity'
  , CONSTRAINT invoice_line_PKC PRIMARY KEY (invoice_line_id)
  , CONSTRAINT invoice_line_FK1 FOREIGN KEY (invoice_id)
    REFERENCES invoice (invoice_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
  , CONSTRAINT invoice_line_FK2 FOREIGN KEY (track_id)
    REFERENCES album.track (track_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) COMMENT 'invoice_line' ;

CREATE INDEX invoice_line_IX1
  ON invoice_line(invoice_id);

CREATE INDEX invoice_line_IX2
  ON invoice_line(track_id);

