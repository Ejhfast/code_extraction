# Remove just the alphabet characters from a string
&gt;&gt;&gt; s = "dsafsadf_afasa_2.2.14_43.33_dsfd"
&gt;&gt;&gt; re.sub(r'[a-z]|(?&lt;=\D)_(?=\d)|(?&lt;=\d)_(?=\D)|(?&lt;=\D)_(?=\D)|^_+|_+$', '', s)
'2.2.14_43.33'
