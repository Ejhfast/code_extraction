# How do I format an MD5 hash with dashes between pairs of digits in python?
&gt;&gt;&gt; x = 'b8f58c3067916bbfb50766aa8bddd42c' # your md5
&gt;&gt;&gt; '-'.join(a + b for a, b in zip(x[0::2], x[1::2])).upper()
'B8-F5-8C-30-67-91-6B-BF-B5-07-66-AA-8B-DD-D4-2C'
