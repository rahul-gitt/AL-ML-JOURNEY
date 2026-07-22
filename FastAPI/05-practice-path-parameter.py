from fastapi import FastAPI

app = FastAPI()

accounts = {
    12345: {"name": "Rahul", "balance": 25000, "account_type": "Savings"},
    12346: {"name": "Rohan", "balance": 100000, "account_type": "Current"},
    12347: {"name": "Amit", "balance": 5000, "account_type": "Savings"}
}

@app.get("/customer/{customer_id}")
def get_customer_id(customer_id : int):
    if customer_id not in accounts:
        return{
            "error" : f"Customer {customer_id} not found."
        }

    customer = accounts[customer_id]

    return {
        "name" : customer['name'],
        'customer id' : customer_id,
        'balance' : customer['balance'],
    }
