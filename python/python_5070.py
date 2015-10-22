# Python conversion from list to tuple
before = ['JACKIE:34', 'MATT:444', 'CEN:12', 'PETE:12', 'RANDY:92', 'MITCH:2', 'JAN:2']
after = [(name, int(value)) for name, value in (x.split(':') for x in before)]
print after
