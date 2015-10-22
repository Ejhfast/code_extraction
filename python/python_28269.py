# Is there any way to check whether an ordinal position contains a character or is empty?
&gt;&gt;&gt; import unicodedata
&gt;&gt;&gt; unicodedata.category(unichr(0x08C0))
'Cn'
