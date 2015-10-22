# Unshorten Flic.kr URLs
&gt;&gt;&gt; import requests
&gt;&gt;&gt; requests.head("https://flic.kr/p/qf3mGd", allow_redirects=True, verify=False).url
u'https://www.flickr.com/photos/106783633@N02/15911453212/'
