import google.generativeai as genai

genai.configure(api_key='AIzaSyBoX_a2R-iVE9T0hB9HAbajDAua9vAzIxs')

model = genai.GenerativeModel('gemini-2.5-flash')

response = model.generate_content("Hello! What is AI?")

print(response.text)