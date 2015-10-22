# How to convert integer value to array of four bytes in python
&gt;&gt;&gt; [hex(0x12345678 &gt;&gt; i &amp; 0xff) for i in (24,16,8,0)]
['0x12', '0x34', '0x56', '0x78']
