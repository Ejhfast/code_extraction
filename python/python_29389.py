# How do I reverse a string in place with Python
def reverseStr(s):
  return ' '.join([x[::-1] for x in s.split(' ')])
