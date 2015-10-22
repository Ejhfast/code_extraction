# pysqlite not accepting qmark parameterization
command = "select id, l from testDT where l like ? "
cur.command(command, ('%, 123]',))
