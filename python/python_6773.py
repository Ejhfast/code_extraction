# How to design a program with many configuration options?
def f(x,y,opt_a=None, opt_b=None):
    if opt_a is None: opt_a = rcParams['group1.opt_a']
