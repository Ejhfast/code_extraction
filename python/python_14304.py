# Injecting HTML into a page using Mechanize
response = br.open("www.linknotonpagethatiwanttogoto.com")
page = response.read()
