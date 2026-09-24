from openai import OpenAI
import hexotools

ollama = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")

def main():
    models_page = ollama.models.list()
    models_list = models_page.data
    model_options = [model.id for model in models_list]

    chosen = hexotools.multiChoice(*model_options)
    
    if chosen is None or chosen[1] is None:
        print("Selection cancelled...")
        return

    chat_history = []

    # The number includes both user & ai responses (e.g. 10 = 5 user & 5 ai responses)
    MAX_MEM = 10

    while True:
        user_prompt = input("[You] ")
        
        if user_prompt.lower() in ("exit", "quit", "q"):
            break
        
        chat_history.append({"role": "user", "content": user_prompt})

        recent_history = chat_history[-MAX_MEM:]

        payload = [{"role": "system", "content": "You are a helpful, brief AI assistant that responds in plaintext, not markdown."}] + recent_history

        response = ollama.chat.completions.create(
            model=chosen[1],
            messages=payload
        )

        response = response.choices[0].message.content
        
        print(f"\n[AI] {response.lstrip()}\n")

        chat_history.append({"role": "assistant", "content": response})
    
if __name__ == "__main__":
    main()
