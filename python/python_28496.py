# What is the Pythonic way of doing this?
&gt;&gt;&gt; dataList = ['Jim    5656    qwgh', 'Tim    5833    qwgh']
&gt;&gt;&gt; [dict(zip(['name', 'sknum'], s.split())) for s in dataList]
[{'name': 'Jim', 'sknum': '5656'}, {'name': 'Tim', 'sknum': '5833'}]
