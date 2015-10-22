# Dictionary Key Error
&gt;&gt;&gt; result = [[1, 'a', 'b'], [2, 'c', 'd']]
&gt;&gt;&gt; dict([(row[0], row[1:]) for row in result])
{1: ['a', 'b'], 2: ['c', 'd']}
