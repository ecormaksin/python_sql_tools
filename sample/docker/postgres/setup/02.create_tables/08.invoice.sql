CREATE TABLE invoice.invoice (
  invoice_id BIGINT NOT NULL
  , customer_id BIGINT NOT NULL
  , invoice_date date NOT NULL
  , billing_address character varying(70)
  , billing_city character varying(40)
  , billing_state character varying(40)
  , billing_country character varying(40)
  , billing_postal_code character varying(10)
  , total integer NOT NULL
  , CONSTRAINT invoice_PKC PRIMARY KEY (invoice_id)
  , CONSTRAINT invoice_FK1 FOREIGN KEY (customer_id)
    REFERENCES customer.customer (customer_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ;

CREATE INDEX invoice_IX1
  ON invoice.invoice(customer_id);

CREATE INDEX invoice_IX2
  ON invoice.invoice(invoice_date);

COMMENT ON TABLE invoice.invoice IS 'invoice';
COMMENT ON COLUMN invoice.invoice.invoice_id IS 'invoice_id';
COMMENT ON COLUMN invoice.invoice.customer_id IS 'customer_id';
COMMENT ON COLUMN invoice.invoice.invoice_date IS 'invoice_date';
COMMENT ON COLUMN invoice.invoice.billing_address IS 'billing_address';
COMMENT ON COLUMN invoice.invoice.billing_city IS 'billing_city';
COMMENT ON COLUMN invoice.invoice.billing_state IS 'billing_state';
COMMENT ON COLUMN invoice.invoice.billing_country IS 'billing_country';
COMMENT ON COLUMN invoice.invoice.billing_postal_code IS 'billing_postal_code';
COMMENT ON COLUMN invoice.invoice.total IS 'total';

CREATE TABLE invoice.invoice_line (
  invoice_line_id integer NOT NULL
  , invoice_id BIGINT NOT NULL
  , track_id BIGINT NOT NULL
  , unit_price numeric(9, 2) NOT NULL
  , quantity integer NOT NULL
  , CONSTRAINT invoice_line_PKC PRIMARY KEY (invoice_line_id)
  , CONSTRAINT invoice_line_FK1 FOREIGN KEY (invoice_id)
    REFERENCES invoice.invoice (invoice_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
  , CONSTRAINT invoice_line_FK2 FOREIGN KEY (track_id)
    REFERENCES album.track (track_id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ;

CREATE INDEX invoice_line_IX1
  ON invoice.invoice_line(invoice_id);

CREATE INDEX invoice_line_IX2
  ON invoice.invoice_line(track_id);

COMMENT ON TABLE invoice.invoice_line IS 'invoice_line';
COMMENT ON COLUMN invoice.invoice_line.invoice_line_id IS 'invoice_line_id';
COMMENT ON COLUMN invoice.invoice_line.invoice_id IS 'invoice_id';
COMMENT ON COLUMN invoice.invoice_line.track_id IS 'track_id';
COMMENT ON COLUMN invoice.invoice_line.unit_price IS 'unit_price';
COMMENT ON COLUMN invoice.invoice_line.quantity IS 'quantity';
