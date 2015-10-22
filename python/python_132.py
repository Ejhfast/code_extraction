# Does c# have anything comparable to Python's list comprehensions
List&lt;Foo&gt; fooList = new List&lt;Foo&gt;();
IEnumerable&lt;Foo&gt; extract = from foo in fooList where foo.Bar &gt; 10 select Foo.Name.ToUpper();
