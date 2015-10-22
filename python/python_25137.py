# creating multiple generators from single loop
compounded_iter = ( (foo.value,bar.value(foo)) for foo in foos)
iter1,iter2 = zip(*compounded_iter)
