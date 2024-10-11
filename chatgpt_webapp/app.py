import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)

# Set your OpenAI API key from the environment variable

def chat_with_gpt(prompt):
    try:
        # New structure for API call in openai>=1.0.0
        chat_completion = client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant. Respond only in haikus."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="gpt-3.5-turbo")
        return chat_completion.choices[0].message.content  # Accessing content from response
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Sorry, I encountered an error."

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = chat_with_gpt(user_input)
        return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html", user_input="", response="")

if __name__ == "__main__":
    app.run(debug=True)
