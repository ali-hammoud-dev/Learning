class ErrorException(ValueError):
    pass

class Book:
    def __init__(self, name:str, page_count:int):
      self.name = name
      self.page_count = page_count
      self.pages_read = 0
      
    def __repr__(self) -> str:
       return(f"Book {self.name} , read {self.pages_read} Pages out of {self.page_count}")
   
    def read(self,pages:int):
        if self.pages_read + pages > self.page_count:
            raise ErrorException(f"Pages Read {self.pages_read} is greater than Pages count {self.page_count}")
        
        self.pages_read += pages
        print(f"you have read {self.pages_read} pages out of {self.page_count}")
        
        
p1 = Book("book 1", 150)
try:
    p1.read(100)
    p1.read(100)
except Exception as e:
    print(e)