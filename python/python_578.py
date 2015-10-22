# Getting a list of specific index items from a list of dictionaries in python (list comprehension)
&gt;&gt;&gt; listDict = [{'id':1,'other':2},{'id':3,'other':4},{'id':5,'other':6}]
&gt;&gt;&gt; [item["id"] for item in listDict]
[1, 3, 5]
