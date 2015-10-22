# How do I write a complex regex as string in python3?
&gt;&gt;&gt; re.compile(r'(?&lt;!\\)(?:(\')|")(?(1)(\\\'|[^\'\r])+?\'|(\\"|[^\r"])+?")')
&lt;_sre.SRE_Pattern object at 0x242aa60&gt;
