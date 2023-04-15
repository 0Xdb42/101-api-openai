#!/usr/bin/env python3
import os
import openai

class OpenAI_BOT:
    """ """
    def __init__(self):
        """ """
        print("~[ Welcome to chatGPT 3.5 Turbo in CLI ]~")
        self.api_key = os.getenv("OPENAI_API_KEY", None)

    def infinite_prompt(self):
        """ """
        history = []
        system = {'role': 'system', 'content': 'you are a helpful assistant.'}
        history.append(system)
        while True:
            prompt = input("> ")
            if prompt == "exit":
                break
            message = {"role":"user", "content":prompt}
            history.append(message)
            try:
                reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=history)
            except openai.error.AuthenticationError:
                print("~[ Erreur d'authentification ]~")
                break
            content = reply['choices'][0]['message']['content']
            history.append({"role":"assistant", "content":content})
            print(f"< {content}\n")
        print("~[ Bye !]~")
        return

def main():
    bot = OpenAI_BOT()
    bot.infinite_prompt()

if __name__ == "__main__":
    main()
