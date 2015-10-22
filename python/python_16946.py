# The elegant way to replace specific characters in Python
star_pos = my_string.find('*')
my_string = my_string[:star_pos] + '*' + checksum_str + my_string[star_pos + 3:]
