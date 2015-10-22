# Using python to match wildcard-expanded string if not proceeded by substring
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall("(?&lt;![\^ACGT])[ACGT]+", "43CGT^TGC35TG^G45C")
['CGT', 'TG', 'C']
