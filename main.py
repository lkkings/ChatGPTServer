from fastapi import FastAPI, Request, Body
from chatgpt import chatbot
from jwt import check_jwt_token
from utils import PermissionNotEnough

app = FastAPI()


@app.post("/chat", summary="ChatGPT接口")
async def chat(request: Request, p: str = Body("", title="发言", embed=True)):
    if "authorization" not in request.headers.keys():
        raise PermissionNotEnough()
    else:
        token = request.headers.get("authorization")
        print(token)
        payload = await check_jwt_token(token)
        if "user" not in payload["scopes"]:
            raise PermissionNotEnough()
        response = chatbot.ask(p, conversation_id=payload["sub"])
        return response["choices"][0]["text"]
