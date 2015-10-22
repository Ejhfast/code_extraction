# Python output to CSV
with open('/home/kwal0203/Desktop/eggs.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hello my friend"])
