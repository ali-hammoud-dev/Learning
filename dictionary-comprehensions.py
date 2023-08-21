
# list of tuples
users = [
     (1, "a", "Alice") ,
     ( 2, "b", "Bob"),
     ( 3, "c", "Charlie"),
     ( 4, "d", "David")
]

username_mapping = {user[1]: user for user in users}
# print(username_mapping)
# print(username_mapping["a"])

x = input("username: ")
y = input("password: ")

_, username, password = username_mapping[x]

if(y) == password:
     print("Correct")
else:
     print("incorrect")


# users = [
#      {"id": 1, "name": "Alice", "password": "alice123"},
#      {"id": 2, "name": "Bob", "password": "bob456"},
#      {"id": 3, "name": "Charlie", "password": "charlie789"},
#      {"id": 4, "name": "David", "password": "david987"}
# ]
