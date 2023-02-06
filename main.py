from fastapi import FastAPI
from chatgpt import chatbot

app = FastAPI()


@app.get("/chat")
async def chat(prompt: str = "", id: int = None):
    response = chatbot.ask(prompt,conversation_id=id)
    print(prompt)
    return response
