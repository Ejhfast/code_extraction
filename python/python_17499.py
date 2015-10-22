# Iterate dicts and extract values without a for loop
&gt;&gt;&gt; lis = [{'year': 2012L}, {'year': 2013L}, {'year': 2013L}, {'year': 2013L}]
&gt;&gt;&gt; [x['year'] for x in lis]
[2012L, 2013L, 2013L, 2013L]
