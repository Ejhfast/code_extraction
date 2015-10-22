# PyYAML interprets string as timestamp
&gt;&gt;&gt; import yaml
&gt;&gt;&gt; yaml.load('time: "10:01"')
{'time': '10:01'}
