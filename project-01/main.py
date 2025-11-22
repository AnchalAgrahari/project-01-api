from fastapi import FastAPI 

app = FastAPI()

@app.get("/api/v1/health")
async def read_root():
    return {"Hello" : "I'm Healthy"}

@app.get("/api/v1/welcome")
async def welcome():
    return {"Message" : "Welcome to FastAPI Application"}



