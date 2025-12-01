import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('AIzaSyBoX_a2R-iVE9T0hB9HAbajDAua9vAzIxs')

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')

chat = model.start_chat(history=[])

print("Gemini Console Chat (type 'quit' to exit)")
print("-" * 50)

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    response = chat.send_message(user_input)
    print(f"AI: {response.text}\n")