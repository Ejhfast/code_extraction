# Matching specific Apache VirtualHost with regex
&lt;VirtualHost \*:[0-9]*&gt;(?:.(?!&lt;/VirtualHost))*?ServerName +desired\.dev(?:(?!&lt;/VirtualHost).)*?&lt;/VirtualHost&gt;
