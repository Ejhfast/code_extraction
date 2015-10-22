# Format string in python with variable formatting
for item, qty in cart.items():
    print "{0:{1}} - {2}".format(item, column_width, qty)
