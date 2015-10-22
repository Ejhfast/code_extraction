# Working with ancestors in GAE
page_key = ndb.Key(Book, bookId, Chapter, chapterId, Page, pageId)
page = page_key.get()
