# Splitting string from character to character
&gt;&gt;&gt; a = "&lt;some_tag&gt;Characters_with_different_len_to_split&lt;/some_tag&gt;"
&gt;&gt;&gt; re.sub(r'&lt;[^&lt;&gt;]*&gt;', '', a)
'Characters_with_different_len_to_split'
