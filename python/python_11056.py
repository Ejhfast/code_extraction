# What command(s) does `heroku pgbackups:capture` run on the server to perform backups?
$ PGPASSWORD=mypassword pg_dump -Fc --no-acl --no-owner -h myhost -U myuser mydb &gt; mydb.dump
