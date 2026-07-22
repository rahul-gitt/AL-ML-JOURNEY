from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Studentadmission(BaseModel):
    name : str
    age : int
    marks : float

@app.post('/admission')
def admission(id : Studentadmission):

    if id.age > 18 and id.marks > 60:
        decision = "You are welcome to the College"

    else:
        decision = "You are rejected"

    return {
        "Age" : id.age,
        "Marks" : id.marks,
        "decision" : decision
    }