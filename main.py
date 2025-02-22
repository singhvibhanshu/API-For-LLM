from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv() # loads a value from our environment variables

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}

def verify_api_key(api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, OR No Credits")
    
    return api_key

app = FastAPI()

@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[api_key] -= 1
    response = ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}])
    return{"response": response["message"]["content"]}