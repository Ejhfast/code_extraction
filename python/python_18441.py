# Written csv file with Python contains wrong format of numbers
sample_means = [x/seg_len] + [mean(data[x:x+seg_len,i]) for i in range(4)]
writer.writerow(sample_means)
