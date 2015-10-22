# Something like optionalQuotedString in pyparsing?
def quotedStringOrWord(pattern):
    return quotedString(pattern) | Word(pattern)
