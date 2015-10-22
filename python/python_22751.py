# How to do GOOD right justify in python? the string before str.rjust() has various length
print((str(unique_emails[x]) + ": ").ljust(20) +
      str(my_emails.count(unique_emails[x])).rjust(4))
