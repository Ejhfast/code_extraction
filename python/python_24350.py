# Pushing results of Imaplib to Mysql database leading to "TypeError"
con.cursor().execute("INSERT INTO email VALUES (%s,%s,%s,%s)",
 (buffer(str(email_to)),buffer(str(email_from)),buffer(str(email_header)),buffer(str(email_msg))))
