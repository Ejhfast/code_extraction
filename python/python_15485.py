# Using Key in NDB to retrieve an entity
chapter_key = ndb.Key('Book', long(bookId), 'Chapter', long(chapterId))
page = Page.query(Page.pageNumber==pageNumber, ancestor=chapter_key)
