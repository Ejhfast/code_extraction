# regex groups to find a range
&gt;&gt;&gt; re.search('( &lt; (?P&lt;min&gt;\d+)| &gt; (?P&lt;max&gt;\d+))+', 'age &lt; 4 &gt; 6').groupdict()
{'max': '6', 'min': '4'}
