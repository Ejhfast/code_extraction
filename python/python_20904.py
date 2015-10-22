# Python Regex to capture single character alphabeticals
print re.compile(^[(,\[]?[a-z][),;\]]?[,;]?$).search('(s)')
