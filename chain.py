import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

user_input = input("You: ")

try:
    response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_input}\nPlease provide a concise answer."}
        ],
        max_tokens=512,
        temperature=0.7
    )
    reply = response["choices"][0]["message"]["content"].strip()
    print(f"chatbot: {reply}\n")
except Exception as e:
    print("Error:", e)
