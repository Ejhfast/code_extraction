# The jsonpickle converts my dictionary keys from numbers to strings
&gt;&gt;&gt; import msgpack
&gt;&gt;&gt; type(msgpack.unpackb(msgpack.packb({12: 23})).keys()[0])
&lt;type 'int'&gt;
