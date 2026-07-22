from fastapi import FastAPI

app = FastAPI()

customer_profile = {
    101: {"name" : "Rahul Mondal", "risk": "mid", "score" : 460},
    102: {"name": "Debabrata Pan", "risk": "high", "score" : 570},
    103: {"name" : "Subha Kayal", "risk" : "low", "score": 90}
}

@app.get("/customer/{customer_id}")
def get_customer(customer_id : int):
    if customer_id not in customer_profile:
        return {
            "error" : f"customer {customer_id} not found."
        }

    customer = customer_profile[customer_id]

    return {
        "name" : customer['name'],
        "Id" : customer_id,
        "score" : customer['score']
    }

