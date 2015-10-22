# Python and binary data in regexps
str_with_ainsi_esc = '\x1b[10;10HSalut'
print re.sub('\x1b\[\d+;\d+H','',str_with_ainsi_esc)
