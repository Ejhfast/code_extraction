# How to perform such filter queries in mongoengine on nested dicts or arrays contained in dict with python?
1) Sample.objects(somedict__someinfo__name='Jordan')
2) Sample.objects(somedict__someinfo__food='Fries')
