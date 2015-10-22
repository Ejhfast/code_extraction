# how do I return cell values in a spreadsheet based on user input in Python?
dateInput = raw_input("Date? (MM/DD/YYYY) ").strip()
amount_re = re.compile(r"(^%s)" % (dateInput,))
cell_list = wks.findall(amount_re)
