# Function returns None unexpectedly
if is_word(wordlist,split[0]) == True:
        answer.append((start, -shift))
        return find_best_shifts_rec(wordlist, decodedText, (start+(len(split[0])+1)))
