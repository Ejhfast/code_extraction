# MySQLdb input where strings contain string delimiters
cursor.execute('INSERT INTO auth_user (password) VALUES (%s)', [password])
