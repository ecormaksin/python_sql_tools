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
  , CONSTRAINT employee_FK1 FOREIGN KEY (reports_to)
      REFERENCES employee (employee_id)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
) COMMENT 'employee' ;

CREATE INDEX employee_IX1
  ON employee(last_name);

CREATE INDEX employee_IX2
  ON employee(first_name);

CREATE INDEX employee_IX3
  ON employee(email);

CREATE INDEX employee_IX4
  ON employee(reports_to);

