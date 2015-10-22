# How to remove specific symbols from a text using python?
&gt;&gt;&gt; my_str = 'This is my text of 2013-02-11, &amp; it contained characters like this! (Exceptional)'
&gt;&gt;&gt; my_str.translate(None, '!@#%^&amp;*()_+=`/')
This is my text of 2013-02-11,  it contained characters like this Exceptional
