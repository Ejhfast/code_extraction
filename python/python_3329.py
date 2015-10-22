# Python IMAP call
typ, data = imap_conn.fetch(uid, '(BODY.PEEK[TEXT])')
