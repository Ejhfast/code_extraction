# Regular Expression to remove \n outside of curly bracket
&gt;&gt;&gt; re.sub(r'\n(?![^{]*\})', '', text)
