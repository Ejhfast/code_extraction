# Python 3.3 Writing A String From A List To A txt File
with open("StaffData.txt", "wt") as file:
    for contacts in staffList :
       file.write("\n".join(str(contacts).split(' - ')) + "\n")
