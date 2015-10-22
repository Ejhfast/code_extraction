# Compare beginning of strings of a list with a whitelist
&gt;&gt;&gt; [item for item in my_list if not item.startswith(whitelist)]
['three']
