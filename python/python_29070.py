# Python: print specific attributes using for loop
for x in ['func_closure','func_code','func_defaults','func_dict']:
     y = getattr(MyFunc.data,x)
     print y
