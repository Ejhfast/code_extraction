# Regex in Python 2.7 for extraction of information from Snort log files
&gt;&gt;&gt; m = re.search(r'\[Classification:\s*([^]]+)\]', line).group(1)
