# What code does Python's timeit(...) method actually time in this bit of code?
timeit.timeit("A0(aList)", setup="from HW2 import A0; aList = [randint(1,256) * (-1) ** randint(1,2) for j in range("+str(n)+")] ", number=1000000)
