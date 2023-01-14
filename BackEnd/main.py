import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return {"message":"welcome in the calculator"}

@app.get('api/calculator/sum/{num1}/{num2}')
def get_root(num1:float, num2:float):
    return {f"sum({num1}, {num2})":f"{num1+num2}"}

@app.get('api/calculator/diff/{num1}/{num2}')
def get_root(num1:float, num2:float):
    return {f"diff({num1}, {num2})":f"{num1-num2}"}

@app.get('api/calculator/prod/{num1}/{num2}')
def get_root(num1:float, num2:float):
    return {f"prod({num1}, {num2})":f"{num1*num2}"}

@app.get('api/calculator/div/{num1}/{num2}')
def get_root(num1:float, num2:float):
    return {f"dif({num1}, {num2})":f"{num1/num2}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")