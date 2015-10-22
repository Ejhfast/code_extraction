# parsing html using pcre in python re module
temp=re.finditer(r"&lt;p&gt;[^\"\&amp;\;]*?&lt;\/p&gt;\s*&lt;ul&gt;\s*&lt;li&gt;\d(.|\s)*?&lt;\/ul&gt;",html)
    for match in temp:
        print match.group(0)
