from fastapi import FastAPI, HTTPException # type: ignore
from google import genai
from google.genai import types
from IPython.display import HTML,Markdown,display
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.post("/")
def read_root():
    return {"Hello": "World"}

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain AI to me like I'm a kid.")

print(response.text)