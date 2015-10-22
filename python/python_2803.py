# Extracting date from a string in Python
match = re.search(r'\d{4}-\d{2}-\d{2}', text)
date = datetime.strptime(match.group(), '%Y-%m-%d').date()
