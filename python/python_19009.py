# Algorithm similar to 'Fizzbuzz'
def process_list(mylist):
    return [(-3 if x % 15 == 0 else (-2 if x % 5 == 0 else ( -1 if x % 3 == 0 else x))) for x in mylist if isinstance(x, int)]
