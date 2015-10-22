# Alternative to Double Iteration
my_list = [y for y in my_list
             if not any(meets_requirement(x,y) for x in my_list)]
