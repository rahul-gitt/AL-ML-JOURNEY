from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "My FastAPI is working."}

@app.get('/get_things/{id}')
def get_things(id : int):
    products = ['Mouse', 'Keybord', 'Monitor', 'UPS', 'Mobile']
    return products[id]