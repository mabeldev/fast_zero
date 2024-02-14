from fastapi import FastAPI

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=200, response_model=Message)
def read_root():
    message = Message(detail='Olá Mundo!')
    return message
