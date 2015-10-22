# How does this python script see the correct column?
with open(input_file) as f:
   reader = csv.DictReader(f)
   cars_list = tuple([row["Model"] for row in reader])
