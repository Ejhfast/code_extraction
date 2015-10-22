# how to count how many letters in my Junk in gmail?
con.select("[Gmail]/Spam") # for the label "Sent" use: "[Gmail]/Sent Mail"
status, data = con.search(None, "ALL")
print len(data[0].split()) # prints the number of msgs in your Spam
