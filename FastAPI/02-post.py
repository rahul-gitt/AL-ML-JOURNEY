from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Loanapplication(BaseModel):
    age : int
    income : float
    loan_ammount : float
    employment_years : float

@app.post('/predict')
def predict_loan(application : Loanapplication):

    if application.income> 50000 and application.employment_years > 3:
        decision = "Approved"

    else:
        decision = "Rejected"

    return {
        "application_age" : application.age,
        "decision" : decision 
    } 