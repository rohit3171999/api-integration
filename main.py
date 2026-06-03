from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Working fine!"}

students = [
    {"id": 1, "name": "Rohit"},
    {"id": 2, "name": "Aman"},
    {"id": 3, "name": "Priya"}
]

items = [
    {"id": 1, "name": "x"},
    {"id": 2, "name": "y"},
    {"id": 3, "name": "z"}
]

@app.get("/students")
def get_students():
    return students 

@app.get("/items")
def get_items():
    return items 