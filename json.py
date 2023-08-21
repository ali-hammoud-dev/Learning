# Assume we have a dictionary called 'transaction' with some data
transaction = {
    "payload": {
        "account_number_id": 12345,
        "amount": 100.00,
        "description": "Payment"
    },
    "Hello": {
        "world": "string"
    },

    "sikinawnaw": "ali hamoud",
    "count": 1
}

transaction1 = {
    "payload": {
        "old_source_reference_number": "ABC123",
        "amount": 150.00,
        "description": "Refund"
    }
}

old_source_reference_number = transaction1["payload"]["old_source_reference_number"]
test = transaction["payload"].get("description")
test2 = transaction1["payload"].get("old_source_reference_number")
test3 = transaction["sikinawnaw"]
test4 = transaction.pop("count")


print(transaction)
print(test4)
