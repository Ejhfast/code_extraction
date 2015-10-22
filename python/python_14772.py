# (Python) Parsing tab delimited strings with newline characters
data = 'Field_1 \t Field_2 \t Field_3 \n Additional Text \n More text \t Field_4'
print data.split('\t')
