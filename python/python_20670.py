# Python CSV skip or delete 2nd row
out_csv.writerow(next(in_txt)) # headers
next(in_text) # skip
out_csv.writerows(in_txt) # write remaining
