# From matrix to list of words
&gt;&gt;&gt; [' '.join(word for include_word, word in zip(row, words) if include_word)
     for row in matrix]
['.net', 'python .net', 'c++ .net']
