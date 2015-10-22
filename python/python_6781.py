# removing random whitespace
sentence = 'I    live in  Virginia   and it is  raining     today'
' '.join([segment for segment in sentence.split()])
