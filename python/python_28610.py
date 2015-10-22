# Filtering a list of strings with list of keywords using loops
&gt;&gt;&gt; [[word for word in string.split() if word in keywords] for string in stringlist]
[['dog', 'cat', 'dog', 'old'], ['dog', 'old']]
