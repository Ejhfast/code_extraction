# Python if-statement based on content of HTML title tag
m = re.search('&lt;title&gt;(.*?)&lt;/title&gt;', html)
if m:
    title = m.group(1)
