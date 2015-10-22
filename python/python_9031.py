# sqlite3 unrecognized token error for ( md5 or sha1)
&gt;&gt;&gt; table_name = "table%s" % hashlib.sha1('blurp').hexdigest()
&gt;&gt;&gt; print(table_name)
table5187399948bdcff4fa10220cd8509257567c6b5a
