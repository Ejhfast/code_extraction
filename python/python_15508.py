# Python bytes literal has extra characters that aren't hex, but alter the value of the string
&gt;&gt;&gt; b'\x12\x41\x42'
b'\x12AB'
