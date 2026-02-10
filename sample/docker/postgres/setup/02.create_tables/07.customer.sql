CREATE TABLE customer.customer (
  customer_id BIGINT NOT NULL
  , first_name character varying(40) NOT NULL
  , last_name character varying(40) NOT NULL
  , company character varying(80)
  , address character varying(70)
  , city character varying(40)
  , state character varying(40)
  , country character varying(40)
  , postal_code character varying(10)
  , phone character varying(24)
  , fax character varying(24)
  , email character varying(320) NOT NULL
  , support_rep_id BIGINT
  , CONSTRAINT customer_PKC PRIMARY KEY (customer_id)
  , CONSTRAINT customer_FK1 FOREIGN KEY (support_rep_id)
      REFERENCES employee.employee (employee_id)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
) ;

CREATE INDEX customer_IX1
  ON customer.customer(first_name);

CREATE INDEX customer_IX2
  ON customer.customer(last_name);

CREATE INDEX customer_IX3
  ON customer.customer(email);

CREATE INDEX customer_IX4
  ON customer.customer(support_rep_id);

COMMENT ON TABLE customer.customer IS 'customer';
COMMENT ON COLUMN customer.customer.customer_id IS 'customer_id';
COMMENT ON COLUMN customer.customer.first_name IS 'first_name';
COMMENT ON COLUMN customer.customer.last_name IS 'last_name';
COMMENT ON COLUMN customer.customer.company IS 'company';
COMMENT ON COLUMN customer.customer.address IS 'address';
COMMENT ON COLUMN customer.customer.city IS 'city';
COMMENT ON COLUMN customer.customer.state IS 'state';
COMMENT ON COLUMN customer.customer.country IS 'country';
COMMENT ON COLUMN customer.customer.postal_code IS 'postal_code';
COMMENT ON COLUMN customer.customer.phone IS 'phone';
COMMENT ON COLUMN customer.customer.fax IS 'fax';
COMMENT ON COLUMN customer.customer.email IS 'email';
COMMENT ON COLUMN customer.customer.support_rep_id IS 'support_rep_id';
