CREATE TABLE employee.employee (
  employee_id BIGINT NOT NULL
  , last_name character varying(40) NOT NULL
  , first_name character varying(40) NOT NULL
  , title character varying(30)
  , reports_to BIGINT
  , birth_date date
  , hire_date date
  , address character varying(70)
  , city character varying(40)
  , state character varying(40)
  , country character varying(40)
  , postal_code character varying(10)
  , phone character varying(24)
  , fax character varying(24)
  , email character varying(320) NOT NULL
  , CONSTRAINT employee_PKC PRIMARY KEY (employee_id)
  , CONSTRAINT employee_FK1 FOREIGN KEY (reports_to)
      REFERENCES employee.employee (employee_id)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
) ;

CREATE INDEX employee_IX1
  ON employee.employee(last_name);

CREATE INDEX employee_IX2
  ON employee.employee(first_name);

CREATE INDEX employee_IX3
  ON employee.employee(email);

CREATE INDEX employee_IX4
  ON employee.employee(reports_to);

COMMENT ON TABLE employee.employee IS 'employee';
COMMENT ON COLUMN employee.employee.employee_id IS 'employee_id';
COMMENT ON COLUMN employee.employee.last_name IS 'last_name';
COMMENT ON COLUMN employee.employee.first_name IS 'first_name';
COMMENT ON COLUMN employee.employee.title IS 'title';
COMMENT ON COLUMN employee.employee.reports_to IS 'reports_to';
COMMENT ON COLUMN employee.employee.birth_date IS 'birth_date';
COMMENT ON COLUMN employee.employee.hire_date IS 'hire_date';
COMMENT ON COLUMN employee.employee.address IS 'address';
COMMENT ON COLUMN employee.employee.city IS 'city';
COMMENT ON COLUMN employee.employee.state IS 'state';
COMMENT ON COLUMN employee.employee.country IS 'country';
COMMENT ON COLUMN employee.employee.postal_code IS 'postal_code';
COMMENT ON COLUMN employee.employee.phone IS 'phone';
COMMENT ON COLUMN employee.employee.fax IS 'fax';
COMMENT ON COLUMN employee.employee.email IS 'email';
