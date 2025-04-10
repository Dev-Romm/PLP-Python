class Book:
    def __init__(self, author, description, copies=0):
        self.author = author
        self.description = description
        self.copies = copies
    
    def __str__(self):
        return f"Author: {self.author}, Description: {self.description}"
    
    def get_copies(self):
        return f"Number of copies: {self.copies}"
    
class Novel(Book):
    pass
    def __init__(self, author, description, pages=0):
        super().__init__(author, description)
        self.pages = pages
    def __str__(self):
        return f"Author: {self.author}, Description: {self.description}, Pages: {self.pages}"

book1 = Book("J.K. Rowling", "A fantasy novel about a young wizard.", 20)
book2 = Novel("George R.R. Martin", "A fantasy series with complex characters.", 800)

print(book1)
print(book2)
print(book1.get_copies())
print(book2.get_copies())