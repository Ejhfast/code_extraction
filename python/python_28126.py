# How to capture only part of regex
&gt;&gt;&gt; re.search(r';Video=([A-Z]{2})', 'nt;Video=SD-H.264;D').group(1)
'SD'
