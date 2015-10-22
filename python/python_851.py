# Parse Gmail with Python and mark all older than date as "read"
typ, data = M.search(None, '(BEFORE 01-Jan-2009)')
for num in data[0].split():
   M.store(num, '+FLAGS', '\\Seen')
