import os
from openai import OpenAI
from confg  import SamKey





class Film:

    def __init__(self ):
        self.client = OpenAI(
            api_key= SamKey,  # This is the default and can be omitted
        )
    
    def Ai_start(self,text):
        question = text
        chat_completion = self.client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Пришли 5 фильмов которие уже вышли используя эти инструкции: " + question + " Стилизовать для Телеграма",
        }
    ],
    model="gpt-4o",
)
        print(chat_completion.choices[0].message.content)

    
if __name__ == '__main__':
    film = Film()
    film.Ai_start("Всем серии шрека")

