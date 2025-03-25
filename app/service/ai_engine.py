from google import genai
from google.genai import types
from app.config.setting import Settings


GEMINI_API_TOKEN = Settings().GEMINI_API_TOKEN

def get_medical_response(question, max_tokens = 50):
    client = genai.Client(api_key=GEMINI_API_TOKEN)
    medical_prompt = f"""
    You are a highly specialized AI doctor. Only provide responses related to medical and healthcare topics.
    If a question is not related to medicine, respond with:
    "I only provide medical-related information. "


    User's question: {question} Keep responses **concise but complete**
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=medical_prompt,
        config=types.GenerateContentConfig(
            top_p=0.5,            
            max_output_tokens=max_tokens,
            temperature=0.2,
        )
    )
    
    return response.text

