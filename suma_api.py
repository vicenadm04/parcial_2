from fastapi import FastAPI
from suma import suma  
app = FastAPI()

@app.get("/suma")
def sumar(a: int, b: int):
    return {"resultado final": suma(a, *b)}
