# Python utf-8 accents problem
def remove_accents(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
