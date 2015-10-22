# Dhcpd lease matching by using regex in python?
regex = r'(lease\s*[0-9\.]+\s*\{[^\{\}]*%s[^\{\}]*(.*"[^\{\}]*\}|\}))' % mac #mac comes as parameter
m = re.findall(regex,lines)
