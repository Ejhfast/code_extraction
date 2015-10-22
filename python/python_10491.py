# Python regex ordering issue
s_regs = sorted(regexes,key=lambda x:len(x))
s_regs.reverse()
regex = '|'.join(s_regs)
