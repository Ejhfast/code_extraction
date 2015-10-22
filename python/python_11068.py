# string to list of dictionaries (python)
&gt;&gt;&gt; [ dict(y.split(':') for y in x.split(',')) for x in 'name:mickey,age:58|name:minnie,age:47,weight:60'.split('|')]
[{'age': '58', 'name': 'mickey'}, {'age': '47', 'name': 'minnie', 'weight': '60'}]
