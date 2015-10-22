# How can i compare two lists of words, change the words that are in common, and print the result in python?
&gt;&gt;&gt; new_title = ' '.join(w.title() if w not in common else w for w in lst)
&gt;&gt;&gt; new_title = new_title[0].capitalize() + new_title[1:]
'The Man Is in the Barrel'
