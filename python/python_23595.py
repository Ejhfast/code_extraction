# Split comma separater string while escaping the ones in parentheses
ddl = 'org_id bigint,merc_name varchar(50),deposit_day date null,amount decimal(18,3),bank_name varchar(128)'
print re.findall('(?:[^,(]|\(.*?\))+', ddl)
