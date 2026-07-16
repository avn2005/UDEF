def load_prompt(prompt_name):
    with open(f"prompts/{prompt_name}", "r", encoding="utf-8") as file:
        return file.read()
