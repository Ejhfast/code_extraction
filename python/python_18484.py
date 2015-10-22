# Is it possible to format text input so Python recognises it as a list?
&gt;&gt;&gt; ast.literal_eval(raw_input('Foo: '))
Foo: 1,2,3
(1, 2, 3)
