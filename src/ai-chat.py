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
    
    while True:
        user_prompt = input("[You] ")
        
        if user_prompt.lower() in ("exit", "quit", "q"):
            break

        response = ollama.chat.completions.create(
            model=chosen[1],
            messages=[
                {"role": "system", "content": "You are a helpful, brief AI assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        print(f"\n[AI] {response.choices[0].message.content}")
    
if __name__ == "__main__":
    main()
