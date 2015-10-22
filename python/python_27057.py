# Intersection of lists, look for on length
four_letter_intersection = {
    word for word in set(list_a).intersection(list_b) if len(word) == 4
    }
