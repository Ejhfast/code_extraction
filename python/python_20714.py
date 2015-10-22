# Perl regex in Python
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub(r'(\s|^)(\$x)(\s|$)', r'\1$Q\3', '$x start $x bar$xy $$x end $x')
'$Q start $Q bar$xy $$x end $Q'
