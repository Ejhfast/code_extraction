# Fix invalid XML with ampersands in Python
&gt;&gt;&gt; import tidy
&gt;&gt;&gt; print tidy.parseString("&lt;IceCream&gt;Ben&amp;Jerry&lt;/IceCream&gt;", input_xml=True)
&lt;IceCream&gt;Ben&amp;amp;Jerry&lt;/IceCream&gt;
