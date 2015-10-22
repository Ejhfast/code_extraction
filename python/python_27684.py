# for-loop ignores some elements of list, when in combination with if-statement
&gt;&gt;&gt; tikzFiles = ['keepme.tikz', 'inputs.tex', 'bla1.bat', 'bla2.tex', 'bla3.py']
&gt;&gt;&gt; [file for file in tikzFiles if file.endswith('.tikz')]
['keepme.tikz']
