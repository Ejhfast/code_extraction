# Python regex non-capturing issue?
&gt;&gt;&gt; match = re.search(r"(?&lt;=').*?(?=')", "a 'quoted' string. 'second' quote")
&gt;&gt;&gt; print match.group(0)
quoted
