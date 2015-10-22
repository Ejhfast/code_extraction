# Regex to convert path to URL
wrap('HA HA HA /services/nfs_qa/log.lol HO HO HO', '/services/nfs_qa/[^ ]*')
'HA HA HA &lt;a href="/static/services/nfs_qa/log.lol"&gt;Link to the file&lt;/a&gt; HO HO HO'
