# Python Regexp: find all words/phrases within a querystring containing OR and AND
re.split(' OR | AND ', 'word1 AND word2 word3 OR "word4 word5" OR word6 AND word7 word8')
['word1', 'word2 word3', '"word4 word5"', 'word6', 'word7 word8']
