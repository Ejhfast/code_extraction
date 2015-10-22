# In bash, what is the simplest way to configure lighttpd to call a local python script based on a particular URL?
cgi.assign = ( ".py" =&gt; "/usr/bin/python" )
