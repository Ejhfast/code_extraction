# Python match a number within a string
regex = re.compile(r'ORA-16252: unable to extend segment by \d+ in tablespace')
if regex.match(s):
    ...
