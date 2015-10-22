# Python MySQLdb : Duplicate entry '2147483647' for key 1
db_query = cur.execute("INSERT INTO tblS100CurrentListing " +
    "(articleCode, dateReceived, s100RSD, remarks) VALUES (%s, %s, %s, %s)",
    (articleCode, dateReceived, s100rsd, remark_text))
