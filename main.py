from fastapi import FastAPI,Request
import requests

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
load_dotenv(override=True) 

api_key = os.getenv("GROQ_API_KEY")

print("KEY LOADED:", api_key)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

print("KEY:", os.getenv("GROQ_API_KEY"))

app=FastAPI()
@app.get("/")
def home():
    return{
        "msg":"you are on home tab"
        
    }
    
    
@app.post("/generate")
async def generate(req: Request):
    try:
        data = await req.json()
        prompt = data["prompt"]

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

        return {"content": result}

    except Exception as e:
        return {"content": f"Error: {str(e)}"}