from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import os, json, re

# Groq
# load_dotenv(override=True)
# client = OpenAI(api_key=os.environ.get('GROQ_API_KEY'),base_url="https://api.groq.com/openai/v1")

# Ollama
client = OpenAI(api_key="ollama",base_url="http://localhost:11434/v1")

system_prompt = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""

MODEL = "qwen3.5:9b"

def chat(message,history):
    history = [{"role":h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role":"user","content":message}]
    response = client.chat.completions.create(model=MODEL,messages = messages,tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        msg = response.choices[0].message
        responses = handle_tool_calls(msg)

        messages.append({
            "content": msg.content or "",
            "role": msg.role,
            "tool_calls": msg.tool_calls
        })
        messages.extend(responses)

        response = client.chat.completions.create(model=MODEL,messages=messages, tools=tools)
    

    pcsd_output = re.sub(r"<think>.*?</think>", "", response.choices[0].message.content, flags=re.S)

    # f"Reasoning:\n{response.choices[0].message.reasoning}\n\nResponse:\n{pcsd_output.strip()}" if you want reasoning - but it does include it in history which is unoptimal for context window
    return pcsd_output.strip()

ticket_prices = {"london":"£100","paris":"£200","berlin":"£300"}
def get_ticket_price(city):
    print("tool called for",city)
    return f"The price of a ticket to {city} is {ticket_prices.get(city.lower(),"Unknown price")}."

tools = [{"type": "function", "function": {
    "name": "get_ticket_price",
    "description": "Get the price for a ticket to a destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city that goes that the customer wants to travel to"
            },
        },
        "required": ["city"],
        "additionalProperties": False
    }
}}]

def handle_tool_calls(message):
    responses = []
    for i in message.tool_calls:
        if i.function.name == "get_ticket_price":
            args = json.loads(i.function.arguments)
            city = args.get("city")
            responses.append({
                "role": "tool",
                "content": get_ticket_price(city),
                "tool_call_id": i.id
            })
    return responses

gr.ChatInterface(fn=chat).launch()