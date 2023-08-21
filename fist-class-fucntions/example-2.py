from operator import itemgetter

def search(sequence,expected,finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"could not find an eleemnt with {expected}")


def get_friend_name(friend):
    return friend["name"]

friends =[
    {"name":"ali hammoud","age" : 20},
    {"name":"hello world","age" : 20},
    {"name":"bob smith","age" : 20}
]

# for x in friends:
#     print(x)

# print(get_friend_name(friends[0]))

filtered_transactions = filter(lambda x: x['name'] == "ali hammoud", friends)
filtered_transactions_list = list(filtered_transactions)

print(filtered_transactions_list)
print(search(friends,"ali hammoud",get_friend_name))
print(search(friends,"ali hammoud",lambda f: f["name"]))
print(search(friends,"ali hammoud",itemgetter("name")))