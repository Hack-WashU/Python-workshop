import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Chat completion
def chat_with_gpt():
    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant. Respond only in haikus."
        },
        {
            "role": "user",
            "content": "Name the best basketball player and why is it Lebron James."
        }
    ],
    model="gpt-3.5-turbo")

    print("ChatGPT Response:", chat_completion.choices[0].message.content)

if __name__ == "__main__":
    chat_with_gpt()
