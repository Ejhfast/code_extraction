# How to read a .csv file specific items that hold this contrait?
with open('text.csv') as text:
    # iterate the list except for the title line and grab desired items
    data = [a for a, b, c in list(csv.reader(text))[1:] if float(b) &gt; 0]
