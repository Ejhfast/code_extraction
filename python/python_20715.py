# Python string formatting: get value in a dictionary by using index of another keyword
&gt;&gt;&gt; dictionary = {5: "May"}
&gt;&gt;&gt; "{part[1]} {{month[{part[0]}]}} {part[2]}".format(part=string.split('/')).format(month=dictionary)
'11 May 2013'
