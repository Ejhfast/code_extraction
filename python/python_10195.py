# splicing strings in two different way
&gt;&gt;&gt; sentence = "abcdefghijkl"
&gt;&gt;&gt; [sentence[i:i+2] for i in range(len(sentence) - 1)]
['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl']
