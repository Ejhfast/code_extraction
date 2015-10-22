# Convert Unicode string to nested list
&gt;&gt;&gt; [[i.encode('ascii', 'ignore').replace('[', '') for i in x] for x in value]
[['Seba', '10'], ['Gianfranco', '80'], ['Marco', '20'], ['Massimo', '125']]
