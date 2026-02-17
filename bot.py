from google import genai
from google.genai import types

# 1. Initialize the Client
client = genai.Client(api_key="YOUR GEMINI KEY")

# 2. Define the System Instructions
# This forces the model to stay in "Health Mode"
health_system_instruction = """
You are a specialized Health and Wellness Assistant. 
Your expertise is limited strictly to: 
1. General medical information and anatomy.
2. Nutrition, exercise, and wellness advice.
3. Mental health support and resources.

STRICT RULES:
- If a user asks a question NOT related to health (e.g., coding, history, gossip), 
  politely reply: "I am specialized only in health and wellness queries. How can I help you with your health today?"
- ALWAYS include a disclaimer at the end of medical advice: "Disclaimer: I am an AI, not a doctor. Please consult a medical professional for personal health concerns."
- Be empathetic, professional, and evidence-based.
"""

def ask_health_assistant(user_prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", # Best speed/logic for specialized apps
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=health_system_instruction,
            temperature=0.3, # Lower temperature makes the model more focused/less creative
        )
    )
    return response.text

while True:
    query = input("Ask me health related questions only.write exit to quit").lower().strip()
    if query != 'exit':
        response_ = ask_health_assistant(query)
        print(response_)
    else:
        raise KeyboardInterrupt
