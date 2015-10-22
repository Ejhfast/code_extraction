# Serializing a class into json for python/gae
&gt;&gt;&gt; import json
&gt;&gt;&gt; json.dumps(Sample(1, 2, [3, 4], 4, {5: 5, 5: 5}).__dict__)
1: '{"aliases": 4, "locality": [3, 4], "name": 1, "roles": {"5": 5}, "email": 2}'
