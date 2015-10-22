# write xml with beautiful soup
f = open(workbook.name, "w")
f.write(soup.prettify())
f.close()
