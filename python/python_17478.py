# Create Variables Inside Program
name = raw_input("Name the variable:")
value = raw_input("And the value?")
exec("{} = {}".format(name, value))
