# split python string on multiple string delimiters efficiently
&gt;&gt;&gt; re.split(r'\s(?=(?:this|into|ones)\b)', "Let's split this string into many small ones")
["Let's split", 'this string', 'into many small', 'ones']
