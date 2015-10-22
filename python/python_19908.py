# use parameters passed through bottle routes in my SQL SELECT statement
cursor.execute("SELECT this, that WHERE this &gt; %s AND that like %s;", (foo, bar))
