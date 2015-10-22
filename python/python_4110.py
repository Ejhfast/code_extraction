# Python regex string for keyword and keyword options
Regex = re.compile(r'''
^(Rain|Snow|Wind|Standard) &lt;(\d+:\d+|\d+/\d+/\d+)&gt;
''', re.VERBOSE)
