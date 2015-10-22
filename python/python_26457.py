# Separating numbers from symbols in lists; python
numbers = [i for i in the_list if isinstance(i, int)]
symbols = [i for i in the_list if isinstance(i, str)]
