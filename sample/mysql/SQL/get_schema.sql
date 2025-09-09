select
	sq_a.table_name,
	sq_a.column_name,
	sq_a.COLUMN_COMMENT,
	sq_a.IS_NULLABLE,
	sq_a.COLUMN_TYPE,
	case 
		when sq_b.ORDINAL_POSITION is null then ''
		else sq_b.ORDINAL_POSITION
	end as `KEY_POSITION`
from
	information_schema.`COLUMNS` sq_a
	left outer join information_schema.KEY_COLUMN_USAGE sq_b
		on 
		sq_b.TABLE_SCHEMA = sq_a.TABLE_SCHEMA 
		and sq_b.TABLE_NAME = sq_a.TABLE_NAME 
		and sq_b.CONSTRAINT_NAME = 'PRIMARY'
		and sq_b.column_name = sq_a.column_name
where
	sq_a.TABLE_SCHEMA = 'dbeaver_sample'
order by
	sq_a.table_name,
	sq_a.ORDINAL_POSITION
;