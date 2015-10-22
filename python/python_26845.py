# Unit conversion using Python
amount, unit = input('Enter amount with units: ').split()[:2]
converted_data = int(amount) * {'in': 2.54, 'cm': 0.39}[unit]
