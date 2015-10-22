# How can I split a string in Python?
my_str="123456781234567812345678"
splits=[my_str[x:x+8] for x in range(0,len(my_str),8)]
//splits = ["12345678","12345678","12345678"]
