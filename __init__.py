from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz_leitura():
    return {"Teste_Message": "Mensagem de teste"}


@app.get("/items/{item_id}")
def raiz_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
