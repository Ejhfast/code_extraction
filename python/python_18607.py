# control flow for loops that identify chapters in a book
chapters = filter(None,map(str.strip,text.split("\n\n")))
