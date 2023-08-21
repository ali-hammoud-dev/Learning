class BookShelf:
    def __init__(self, *books):
      self.books = books
     
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    

class Book(BookShelf):
    def __init__(self, name):
     self.name = name
     
    def __str__(self):
       return f"Book{self.name}"
   
b1 = Book("harry potter")
b2 = Book("python 101")

print(b1)
print(b2)

sh = BookShelf(b1,b2)

print(sh)
print(*sh.books)


