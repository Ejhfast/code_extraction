# gdb python api: is it possible to make a call to a class/struct method
eval_string = "(*("+str(self.val.type)+"*)("+str(self.val.address)+")).method()"
    return gdb.parse_and_eval(eval_string);
