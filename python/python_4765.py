# RegEx Tokenizer to split a text into words, digits and punctuation marks
txt = "Today it's 07.May 2011. Or 2.999."
regexp_tokenize(txt, pattern=r'\w+([.,]\w+)*|\S+')
['Today', 'it', "'s", '07.May', '2011', '.', 'Or', '2.999', '.']
