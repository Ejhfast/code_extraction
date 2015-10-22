# Replace a pattern in a string once which occurs more than once
&gt;&gt;&gt; re.sub(r'(,\s\w*\s)charlie', r'\1Tony', r"I am Tony not charlie, Hey charlie
 how's you?")
"I am Tony not charlie, Hey Tony how's you?"
