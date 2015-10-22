# How to remove a path prefix in Python?
&gt;&gt;&gt; path = '/book/html/wa/foo/bar/'
&gt;&gt;&gt; path[path.find('/wa'):]
'/wa/foo/bar/'
