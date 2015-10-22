# Re.match always returning None in python
def testChatChars(string):
   return re.match(r'[\x20-\x5A\x5C\x5E-\x7E]+$', string) is not None
