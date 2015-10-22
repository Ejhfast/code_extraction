# Is there a programmatic way to determine whether a PDF's text is extractable using Python?
x = PageObject.getPage(x).extractText())
if (x == ""): #Or whatever exactly you get when it fails.
   raise ValueError("The PDF file can not be imported")
