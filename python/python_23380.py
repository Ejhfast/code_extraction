# Python: remove characters from a string?
&gt;&gt;&gt; string = '3dc8uo8cc33a v8c08oizl6ga'
&gt;&gt;&gt; " ".join("".join(s[2::3]) for s in string.split())
'coca cola'
