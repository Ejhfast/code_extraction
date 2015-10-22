# regex, finding all "href" in <a> tags
re.findall(r'(?&lt;=&lt;a href=")[^"]*',yourStr)
