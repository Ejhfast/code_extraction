# How to remove unconverted data from a Python datetime object
end_date = end_date.split(" ")
end_date[-1] = end_date[-1][:4]
end_date = " ".join(end_date)
