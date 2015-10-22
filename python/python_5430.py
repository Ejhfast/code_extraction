# What's a convenient way of resolving a path /bar/foo/baz/../.. into /bar?
&gt;&gt;&gt; os.path.normpath("/bar/foo/baz/../..")
"/bar"
