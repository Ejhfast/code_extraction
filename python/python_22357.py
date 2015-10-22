# .csv delimiter in between every letter in output
for string in caseStatus.stripped_strings:
            newString = string.replace(" ", "")
            writer.writerow([newString])
