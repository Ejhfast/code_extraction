# Write to a Remote file with Fabric
run('mysqldump [options] | gzip &gt; outputfile.sql.gz')
get('outputfile.sql.gz')
