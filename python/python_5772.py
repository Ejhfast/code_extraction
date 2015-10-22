# elegant way of using a range using an if statement?
for a in range(2, 3000):
    if all(a % k == 0 for k in range(1,11)):
        print a
