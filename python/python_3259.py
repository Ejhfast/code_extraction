# Join string and None/string using optional delimiter
FullName = LastName + (", " + FirstName if FirstName else "")
