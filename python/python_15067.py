# extracting a double from the middle of a string, can't use replace
&gt;&gt;&gt; re.search(r'([\d.]+)\s+#', text).group(1)
'0.0612'
