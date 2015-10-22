# Scrapy - Error Importing JSON
&gt;&gt;&gt; jsonp = response.body
&gt;&gt;&gt; j = jsonp[ jsonp.index("(") + 1 : jsonp.rindex(")") ]
&gt;&gt;&gt; json.loads(j)
