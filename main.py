from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Working Fine!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}
@app.get("/contact")
def contact():  
    return {"message": "Contact us at 9873753135"}   