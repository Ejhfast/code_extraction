# Is there a way to find the second longest word in a sentence in Python?
second_longest = sorted(sentence.split(), key=len)[-2]
