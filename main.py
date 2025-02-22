from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Dictionary to store API keys and their associated credits
API_KEY_CREDITS = {os.getenv("API_KEY"): 5}

# Dependency function to verify API key and check available credits
def verify_api_key(api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(api_key, 0)
    if credits <= 0:
        # Raise an error if the API key is invalid or has no credits left
        raise HTTPException(status_code=401, detail="Invalid API Key, OR No Credits")
    
    return api_key

# Initialize FastAPI application
app = FastAPI()

@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
     # Deduct one credit from the API key's balance
    API_KEY_CREDITS[api_key] -= 1

    # Call the Ollama API to generate a response based on the provided prompt
    response = ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}])

    # Return the generated response
    return{"response": response["message"]["content"]}