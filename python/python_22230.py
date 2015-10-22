# Python: parsing and extracting op-codes from asm
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall(r'\[(?=([a-z0-9.]+))','[slli a3,a3,4] [add.n a3,a3,a8] [l32i a11,a3,128]')
['slli', 'add.n', 'l32i']
