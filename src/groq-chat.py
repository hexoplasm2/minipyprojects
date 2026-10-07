import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

client = OpenAI(
    api_key=os.environ.get('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

completions = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"What's the capital of France?"}
    ]
)

print(completions.choices[0].message.content)