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
  , CONSTRAINT customer_FK1 FOREIGN KEY (support_rep_id)
      REFERENCES employee.employee (employee_id)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
) COMMENT 'customer' ;

CREATE INDEX customer_IX1
  ON customer(first_name);

CREATE INDEX customer_IX2
  ON customer(last_name);

CREATE INDEX customer_IX3
  ON customer(email);

CREATE INDEX customer_IX4
  ON customer(support_rep_id);

