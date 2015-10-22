# How can I use Py3k-style string formatting within Mako templates?
&gt;&gt;&gt; from mako.template import Template
&gt;&gt;&gt; Template("We display two significant digits: ${'{0:.2f}'.format(34.567645765)}").render()
'We display two significant digits: 34.57'
