# Regex for name extraction on text file
&gt;&gt;&gt; regex = re.compile(r'\b([A-Z][a-z]+(?: [A-Z]\.)? [A-Z][a-z]+),')
&gt;&gt;&gt; print regex.findall(text)
['David L. Gallimore', 'Katherine Garduno', 'Russell C. Keller']
