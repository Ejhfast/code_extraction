# Regex how to check last 4 numbers from long number
last4 = str(number)[-4:]
if last4.startswith(('10', '02')):
    print("yes, actually")
