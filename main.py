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

@app.get("/students")
def get_students():
    return students 