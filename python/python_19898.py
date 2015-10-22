# How do i output a single digit as a double digit in python 2.7
for item in my_list2:
    text = map(lambda x: '%02d'%(x,), item)
    ttk.Label(mainframe, text=text).grid(column=0, sticky=W)
