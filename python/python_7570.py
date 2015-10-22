# How can I parse a line by new lines and colons?
data = [line.strip().split(':') for line in data.split('\n') if line.strip()]
