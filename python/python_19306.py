# Counting number of words between punctuation characters in Python
punctuation_i_care_about="?.!"
split_by_punc =  re.split("[%s]"%punctuation_i_care_about, some_big_block_of_text)
words_by_puct = [len(x.split()) for x in split_by_punc]
