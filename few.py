import openai
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/ai/v1"
user_input = input("You:")
reply=""
response = openai.ChatCompletion.create(
    model="mistralai/mistral-7b-instruct", # or another supported model
    message = [
    {"role": "system","content":"You are an expert translator."},
    {"role": "user","content":"English:Good morning\nFrench: Bonjour"},
    {"role": "user","content":f"English: {user_input}\nFrench:"}]
)
reply = response['choices'][0]['message']['content']
print(f"chatbbot:{reply}\n")