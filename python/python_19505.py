# Python: Split string by pattern
&gt;&gt;&gt; s= "{abc, xyz}, 123, {def, lmn, ijk}, {uvw}, opq"
&gt;&gt;&gt; re.findall(r",?\s*(\{.*?\}|[^,]+)",s)
['{abc, xyz}', '123', '{def, lmn, ijk}', '{uvw}', 'opq']
