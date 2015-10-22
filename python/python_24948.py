# Python Regex Findall javascript
In [2]: re.findall(r"(?&lt;=&gt;)[^&lt;]*(?=&lt;/)", "&lt;scrip&gt;hola&lt;/scRIHft&gt; &lt;script=&gt;nano&lt;/script&gt;")
Out[2]: ['hola', 'nano']
