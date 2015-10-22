# Can Regex be used for this particular string manipulation?
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub(r"x(?=[^']*'([^']|'[^']*')*$)", "P", "axbx'cxdxe'fxgh'ixj'k")
"axbx'cPdPe'fxgh'iPj'k"
