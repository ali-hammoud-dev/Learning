class Book:
    TYPES = ("hardcover" , "paperback")
    
    def __init__(self, name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"{self.name} : {self.book_type} : {self.weight}"
    
    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name,cls.TYPES[0],page_weight + 100)
    
    @classmethod
    def paperback(cls,name,page_weight):
        return Book(name,cls.TYPES[1],page_weight + 200)
    
book1 = Book.paperback("hello world",1500)
print(book1)