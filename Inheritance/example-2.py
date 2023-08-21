class Device:
    def __init__(self, name, connectedBy):
      self.name = name
      self.connectedBy = connectedBy
      self.connected = True
      
    def __str__(self):
       return f"Device{self.name!r}({self.connectedBy})"
   
    def disconnect(self):
       self.connected = False
       print("Disconnected !")
       
## means printer inhertited from device
class Printer(Device):
    def __init__(self, name, connectedBy,capacity):
        super().__init__(name,connectedBy)
        self.capacity = capacity
        self.remaining_pages = capacity
        
    def __str__(self):
       return f"{super().__str__()}({self.remaining_pages} pages remaining)"
   
    def print(self,pages):
       if not self.connected:
           print("your printer is not connected!")
           return 
       print(f"Printing {pages} Pages")
       self.remaining_pages -= pages 
       
p1 = Printer("Pinter","USB",500)
p1.print(20)

print(p1)
p1.disconnect()
