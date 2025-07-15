import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google AI Studio API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please add it to your .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

def ask_gpt(prompt: str) -> str:
    """
    Use Google AI Studio's Gemini model to generate responses.
    Renamed from ask_gpt to maintain compatibility with existing code.
    """
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the full prompt with system instruction
        full_prompt = f"You're a helpful educational assistant. {prompt}"
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        return response.text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"
