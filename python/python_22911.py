# How to convert list into a dictionary by python
&gt;&gt;&gt; [{'id':x, 'frame':y, 'length':z} for x,y,z in zip(*old_list)]
[{'length': '5', 'frame': '4', 'id': 'ID0'}, {'length': '6', 'frame': '8', 'id': 'ID1'}]
