# Regex for fixed string followed by characters up to a delimiter character
m = re.search(r'(FullName=.*?),', str)
if m:
   print m.group(1)
