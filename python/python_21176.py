# Recursive regexp in python?
import regex
&gt;&gt;&gt; regex.sub(r'\((((?&gt;[^()]+)|(?R))*)\)', r'del', 'acd (e(fg)h) ij)')
'acd del ij)'
