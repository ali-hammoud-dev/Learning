class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        dictionary = {
            "name":name,"price":price
            }
        self.items.append(dictionary)

    def stock_price(self):
        print(self.items)
        total = 0
        for x in self.items:
            total += x['price']
        print(total)

s1 = Store("ali hammoud")
s1.add_item("ali hsen",25)
s1.add_item("hsen hammoud",30)
s1.stock_price()
