# performing calculations on dictionary values
&gt;&gt;&gt; [x['theint'] + y['theint'] for x, y in zip(*[iter(sorted(adict['key1'].values(), key=operator.itemgetter('thedec')))] * 2)]
[759, 1010, 450]
