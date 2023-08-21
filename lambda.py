# List of dictionaries representing transactions
transaction_list = [
    {"amount": 150.00, "description": "High Amount"},
    {"amount": 200.00, "description": "High Amount"},
    {"amount": 100.00, "description": "Low Amount"}
]

# Use filter() and lambda to get a filtered list of transactions
filtered_transactions = filter(lambda x: x['amount'] > 100.0, transaction_list)

# Convert the filtered_transactions to a list and print it
filtered_transactions_list = list(filtered_transactions)
print(filtered_transactions_list)
