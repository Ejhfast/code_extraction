# Python - dir() - how can I differentiate between functions/method and simple attributes?
[(name,type(getattr(math,name))) for name in dir(math)]
