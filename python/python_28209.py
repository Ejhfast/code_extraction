# Extract names around each word regex
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall(r"([a-zA-Z]+) loves ([a-zA-Z]+)", "Mary loves Mike,Jack loves Lily,Ethan loves Lydia")
[('Mary', 'Mike'), ('Jack', 'Lily'), ('Ethan', 'Lydia')]
