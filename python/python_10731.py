# Is there a way to check a number against all numbers in a list?
if any(n % x == 0 for x in mylist):
    print "Not Prime"
