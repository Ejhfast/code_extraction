# Double single quote into double quote
os.system("psql -h localhost -U postgres -d mabase -c \"COPY tmp_import_csv FROM '/var/www/wwwdata/sum_area.csv' DELIMITER ' ' CSV HEADER;\"")
