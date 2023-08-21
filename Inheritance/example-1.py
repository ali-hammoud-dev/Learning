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
       
printer = Device("Printer", "USB")
print(printer)
print(printer.connected)
printer.disconnect()
print(printer.connected)