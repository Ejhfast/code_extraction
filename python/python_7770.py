# grep prefix python strings
&gt;&gt;&gt; x="the name of 33e4853h45y45 is one of the 33e445a64b65 and we want all the 33e5c44598e46 to be matched"
&gt;&gt;&gt; re.findall("33e\w+",x)
['33e4853h45y45', '33e445a64b65', '33e5c44598e46']
