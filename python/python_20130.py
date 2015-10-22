# How to write unit test for file upload class in django?
&gt;&gt;&gt; c = Client()
&gt;&gt;&gt; with open('wishlist.doc') as fp:
...     c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})
