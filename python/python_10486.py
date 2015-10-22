# mysql user privileges with fabric python regex
run('mysql -u %s -p%s -e "grant all on %s.* to \'%s\'@\'localhost\' identified by \'PASSWORD\'"' % (user, dbpasswd, account, account))
