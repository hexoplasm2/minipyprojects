import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()


# Using groq but any model can be used (that supports OpenAI Client)
client = OpenAI(
    api_key=os.environ.get('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

completions = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Give a long paragraph about lorem ipsum."}
    ],
    stream=True
)

response = ""

with Live(Markdown(response), console=console, refresh_per_second=15) as live:
    for i in completions:
        if x:=i.choices[0].delta.content:
            response+=x
            live.update(Markdown(response))

print()