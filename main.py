from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv() # loads a value from our environment variables

API_KEYS = {os.getenv("API_KEY")}

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    response = ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}])
    return{"response": response["message"]["content"]}