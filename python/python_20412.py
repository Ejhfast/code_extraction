# Python string.translate throws type error for string format (ddd)ddd-dddd
def format_phone(phone_str=None):
    phone_str = phone_str.encode('ascii', 'ignore')
    [...]
