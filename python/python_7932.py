# Python IMAP getting emails before a date, and also UNSEEN
typ, data = conn.search(None, 'BEFORE', before_date, 'UNSEEN')
