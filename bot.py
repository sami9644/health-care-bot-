import os
from openai import OpenAI

# 1. Initialize the OpenAI Client
# You can also set this as an environment variable: export OPENAI_API_KEY='your-key'
client = OpenAI(api_key="your-api-key-here")

# 2. Define the System Guardrail
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a specialized Health & Wellness Assistant. "
        "Provide evidence-based information on health, fitness, and nutrition. "
        "\n\nSTRICT RULES:\n"
        "1. ONLY answer health-related questions. If asked about other topics, "
        "politely decline and state you are only trained for health queries.\n"
        "2. Include a medical disclaimer in your first response of every session.\n"
        "3. If a situation sounds like a medical emergency, advise the user to call emergency services immediately."
    )
}

def start_chatbot():
    # We maintain a list of messages to keep track of conversation history
    messages = [SYSTEM_PROMPT]

    print("--- WellnessBot (Powered by OpenAI) ---")
    print("Ask me anything about health, nutrition, or fitness.")
    print("(Type 'quit' or 'exit' to stop)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Take care of yourself! Goodbye.")
            break

        if not user_input:
            continue

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        try:
            # Generate response
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7 # Slight creativity for natural conversation
            )

            bot_message = response.choices[0].message.content
            print(f"\nBot: {bot_message}\n")
            print("-" * 30)

            # Add assistant message to history to maintain context
            messages.append({"role": "assistant", "content": bot_message})

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_chatbot()
