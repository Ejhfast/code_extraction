# Python CSV read file and select columns and write to new CSV file
for row in reader:
    writer.writerow([row['User Name'],row['Address'].split(',')[0],row['Last Login DateTime'],row['Address'].split(',')[7]])
