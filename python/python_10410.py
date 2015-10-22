# Does ruby have something like python's list comprehensions(example)?
digits.product(chars).select{ |d, ch| d &gt;= 2 &amp;&amp; ch == 'a' }.map(&amp;:join)
