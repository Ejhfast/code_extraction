# String Joining from Iterable containing Strings and ( NoneType / Undefined )
your_list = ['productX', 'deployment-package', '1.2.3.4', None, None, None]
'-'.join(item for item in your_list if item)
