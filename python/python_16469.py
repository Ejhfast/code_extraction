# Processing Result outside For Loop in Python
for eachBrowser in browser_list:
result[eachBrowser]= urllib2.urlopen(urljoin(user_string_url,eachBrowser))
