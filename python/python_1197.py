# Is there a library that can open and search through a pdf file?
pdf = pyPdf.PdfFileReader(file(path, "rb"))
content = pdf.getPage(1).extractText()
