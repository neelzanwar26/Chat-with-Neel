from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks like alexa and gooogle cloud"},
            {"role": "user", "content": "What is machine learning"}
        ]
    )

    print(completion.choices[0].message.content)

except openai.RateLimitError :
    print("⚠️ You exceeded your quota. Please check your OpenAI plan and billing.")