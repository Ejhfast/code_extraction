# Why does Sqlite tell me no such column exists when I plainly created it?
&gt;&gt;&gt; c.execute('''insert into stocks
                 (date, trans, symbol, qty, price)values(?,?,?,?,?)''',
                 ('08-26-1984', 'SELL', 'GOGL', 3, 400.00))
