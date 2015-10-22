# Find and replace nth instance of text string using python or bash
awk -v n=4 '/listen = / &amp;&amp; ++m == n {$3 = "2.2.2.2"} 1' file &gt; file.changed
