# fetch only content of email
status, msg_data = server.fetch(some_id, '(UID BODY[TEXT])')
