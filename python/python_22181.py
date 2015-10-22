# Python testing properties using partial
def test_counter(self):
    book.counter = partial(Book.counter.fget, book)
    self.assertNotEquals(book.counter(), book.counter())
