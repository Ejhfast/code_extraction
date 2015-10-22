# How to print a signed integer as hexadecimal number in two's complement with python?
&gt;&gt;&gt; x=-123
&gt;&gt;&gt; hex(((abs(x) ^ 0xffff) + 1) &amp; 0xffff)
'0xff85'
