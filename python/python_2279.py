# List comprehension from multiple sources in Python?
&gt;&gt;&gt; [(i, j) for i, _, k in myList for j in k]
[('Foo', 1), ('Foo', 2), ('Foo', 3), ('Bar', 'i'), ('Bar', 'j')]
