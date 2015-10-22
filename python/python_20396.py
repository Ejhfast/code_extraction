# replaces multiple occurances of a character (except for first and last) in a python string
str1 = '$2a$10$.XfjKl/,abcd, 1, ##, s, for free,2-3-4'
parts = str1.split(',')
str2 = '{},{},{}'.format(parts[0],'_'.join(parts[1:-1]),parts[-1])
