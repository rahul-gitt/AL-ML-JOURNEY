from fastapi import FastAPI

app = FastAPI()

customer_profile = {
    100 : {"name" : "Rahul Mondal", "risk" : "high", "score" : 720},
    101 : {"name" : "Debabrata Mondal", "risk" : "low", "score" : 980},
    102 : {"name" : "Kakali Mondal", "risk": "mid", "score" : 850}
}

@app.get("/customer/{customer_id}")
def get_customer_id(customer_id : int):
    if customer_id not in customer_profile:
        return {"error" : f"customer {customer_id} not found."}

    profile = customer_profile[customer_id]

    return {
        "customer_id" : customer_id,
        "name" : profile['name'],
        "risk_level" : profile['risk'],
        "score" : profile['score']
    }