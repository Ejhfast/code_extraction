# How do I set a invisible default value in entry widgets?
def num(entry):
    number = Decimal(0.00) if not entry else Decimal(entry)
    return number
