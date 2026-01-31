from openai import OpenAI
import os
client = OpenAI(
    api_key=os.getenv("API_OPENAI")
)

def test_ai():
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
        {"role": "system", "content": "Você é um assistente de teste."},
        {"role": "user", "content": "Diga apenas: conexão OK"}
        ]
    )

    return response.choices[0].message.content