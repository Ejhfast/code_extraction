# Python convert unicode minus sign to float
s = u'\u2212$9.02'
float(s.replace(u'\u2212', '-').replace('$', ''))
