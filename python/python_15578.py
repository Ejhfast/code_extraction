# Python Re, need a list of matches
baseMatch = re.compile('123A[A-Z]{6}')
baseMatch.findall('123AABCDEFxyz123AAABCDExyz')
['123AABCDEF', '123AAABCDE']
