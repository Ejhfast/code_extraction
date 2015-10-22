# Pandas Dataframe apply() method provides a row object, but how do you access the index value
def my_test(row):
   return "{}.{}".format(row.name, row['b'])
