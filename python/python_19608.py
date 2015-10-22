# How to lookup element in AWS response with lxml (namespace issue?)
&gt;&gt;&gt; root.find('.//aws:Quantity', namespaces={'aws': 'http://cloudfront.amazonaws.com/doc/2013-11-11/'})
&lt;Element {http://cloudfront.amazonaws.com/doc/2013-11-11/}Quantity at 0xb6c16aa4&gt;
