# How to byteswap 32bit integers inside a string in python?
&gt;&gt;&gt; input = "12345678abcdeafa"
&gt;&gt;&gt; input[7::-1]+input[:7:-1]
'87654321afaedcba'
