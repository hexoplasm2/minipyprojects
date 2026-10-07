from dotenv import load_dotenv
from openai import OpenAI
from src.libs import hexotools
from rich.live import Live
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.text import Text

# Later planning on adding API support
load_dotenv()
console = Console()

ollama = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")

def main():
    models_page = ollama.models.list()
    models_list = models_page.data
    model_options = [model.id for model in models_list]

    chosen = hexotools.multiChoice(*model_options)
    hexotools.clear()
    
    if chosen is None or chosen[1] is None:
        print("Selection cancelled...")
        return

    chat_history = []

    # The number includes both user & ai responses (e.g. 10 = 5 user & 5 ai responses)
    MAX_MEM = 20

    while True:
        console.print("[bold magenta][You][/]",end=" ")
        user_prompt = input()
        print()
        
        if user_prompt.lower() in ("exit", "quit", "q", "/bye"):
            break
        
        chat_history.append({"role": "user", "content": user_prompt})

        recent_history = chat_history[-MAX_MEM:]

        payload = [{"role": "system", "content": "You are a helpful, brief AI assistant that responds in plaintext, not markdown."}] + recent_history

        response = ollama.chat.completions.create(
            model=chosen[1],
            messages=payload,
            stream=True
        )

        reply = ""
        label = Text("[Hex] ",style="bold yellow")

        with Live(Markdown(reply), console=console, refresh_per_second=15) as live:
            for i in response:
                if x:=i.choices[0].delta.content:
                    reply+=x
                    live.update(Text.assemble(label,reply))
        
        chat_history.append({"role": "assistant", "content": reply})
        print()
    
if __name__ == "__main__":
    main()
