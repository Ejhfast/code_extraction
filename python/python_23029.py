# Regex adding characters before another word (from a list of choices)
&gt;&gt;&gt; t = 'The/O\nSkoll/ORGANIZATION\nFoundation/ORGANIZATION\n,/O\nbased/O\nin/O\nSilicon/LOCATION\nValley/LOCATION\na'
&gt;&gt;&gt; re.sub(r'(/(?:ORGANIZATION|LOCATION|PERSON|O))',r'\t\1', t)
'The\t/O\nSkoll\t/ORGANIZATION\nFoundation\t/ORGANIZATION\n,\t/O\nbased\t/O\nin\t/O\nSilicon\t/LOCATION\nValley\t/LOCATION\na'
