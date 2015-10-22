# Replacing all occurrences of words from a given set, but only if the word is not contained within another word
for word in commonWords :
    text = text.replace(' '+word+' ', ' ')
