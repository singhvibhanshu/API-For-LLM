import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "http://127.0.0.1:8000/generate?prompt=Tell me about the various high level programming language and their most common use cases"
headers = {"api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}

response = requests.post(url, headers=headers)
print(response.json)