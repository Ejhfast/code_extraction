# Python How to find index of second Uppercase letter in a string
m = re.search(r'^([^A-Z]*[A-Z]){2}', 'Paul likes Ice cream.');
print m.span()[1]
12
