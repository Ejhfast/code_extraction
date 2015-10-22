# django,python keyerror from a kwarg key that isn't there - how do i avoid this?
d = dict()
d.get("abc")              #-&gt; None
d.get("abc", "default")   #-&gt; "default"
