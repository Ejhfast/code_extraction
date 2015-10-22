# How to check all the elements in a list that has a specific requirement?
mycards= ['0H','8H','7H','6H','AH','QS']
all((x == 'QS' or 'H' in x) for x in mycards)
#  True
