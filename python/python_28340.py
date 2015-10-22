# How to change value of variable from a different .py file in Python
def changeAge(newAge):
    import bar
    bar.age = newAge
