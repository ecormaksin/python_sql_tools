select
	cols.table_name,
	cols.column_name,
	pd.description as column_comment,
	cols.is_nullable,
	case 
		when cols.data_type = 'numeric' then
			concat(cols.data_type, '(', cast(numeric_precision as text), ', ', cast(numeric_scale as text), ')')
		when cols.data_type = 'character varying' then
			concat(cols.data_type, '(', cast(character_maximum_length as text), ')')
		else cols.data_type
	end as data_type,
	case 
		when kcu.ordinal_position is null then ''
		else cast(kcu.ordinal_position as text)
	end as KEY_POSITION
from
	information_schema.columns as cols
inner join pg_catalog.pg_namespace as ns
  on
	ns.nspname = cols.table_schema
inner join pg_catalog.pg_class as cl
  on
	cl.relname = cols.table_name
	and cl.relnamespace = ns.oid
left outer join pg_catalog.pg_description as pd
  on
	pd.objoid = cl.oid
	and pd.objsubid = cols.ordinal_position
left outer join information_schema.KEY_COLUMN_USAGE kcu
		on 
		kcu.TABLE_SCHEMA = cols.TABLE_SCHEMA
	and kcu.TABLE_NAME = cols.TABLE_NAME
	and kcu.column_name = cols.column_name
where 
	cols.table_schema = 'public'
order by 
	cols.table_name,
	cols.ordinal_position
;
