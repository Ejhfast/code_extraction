# Python collections.Counter How to print element and number of counts
with open(output_file, 'w') as f:
    for word, count in word_list:
        f.write("{0}\t{1}\n".format(word, count))
