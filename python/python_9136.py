# Convert Python None to JavaScript null
&gt;&gt;&gt; import json
&gt;&gt;&gt; json.dumps([1, 2, 3, None, 4])
'[1, 2, 3, null, 4]'
