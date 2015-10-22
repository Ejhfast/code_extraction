# splitting a string->list to be checked
[url for url in urlstring.split(',') if 2 &lt;= len(url.split('.')[-2]) &lt;= 4]
