# Problems using psycopg2 on Mac OS (Yosemite)
$ sudo mv /usr/lib/libpq.5.dylib /usr/lib/libpq.5.dylib.old
$ sudo ln -s /Library/PostgreSQL/9.4/lib/libpq.5.dylib /usr/lib
