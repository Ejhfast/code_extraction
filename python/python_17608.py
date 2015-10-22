# Get list of column names from a Firebird database table
select rdb$field_name from rdb$relation_fields
where rdb$relation_name='YOUR-TABLE_NAME';
