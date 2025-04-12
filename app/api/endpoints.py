from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Groq client with API key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

@app.get("/amit")
async def amit_function():
    return {"message": "Amit to rand hai"}

class TheInput(BaseModel):
    text: str
    size: int

@app.post("/textsummarizer")
async def duhan(request: TheInput):
    # Check if the input text is empty
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input is required")

    try:
        # Generate the completion using Groq API
        completion = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",  # Use the appropriate model
            messages=[
                {"role": "system", "content": "You are an intelligent and efficient text summarizer. Your task is to read any given long text (from a PDF, article, or copied content) and generate a concise and meaningful summary. Identify the key points, retain the original intent, and present the information in a short, clear, and structured format. Always remove unnecessary details and include only the essential information. The output should always be in clear and proper English, either in bullet points or paragraph form depending on the content."},
                {"role": "user", "content": f"summarize the following in {request.size} line: {request.text}"}
            ],
            temperature=0.9,
            max_tokens=1024,
            top_p=1,
            stream=False  # Get full response at once
        )

        # Extract the summary from the response
        answer = completion.choices[0].message.content if completion.choices else None

        if answer is None:
            raise HTTPException(status_code=500, detail="Summarization failed. No valid response.")

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
