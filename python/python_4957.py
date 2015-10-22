# python+postgresql: Convert string literal to regex
print '.{0,3}'.join(re.escape(part) for part in s.split('?')) + '.*'
