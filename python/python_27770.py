# how to tell python 3 to skip over non-digit characters from a csv file
the_numbers = [float(row[rowNum]) for row in reader if row[rowNum] not in "?"]
    #replace "?" with a string of any strange characters
