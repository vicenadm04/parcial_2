from fastapi import FastAPI
from suma import suma  # Tu función original de suma(a, b)

app = FastAPI()

@app.get("/suma")
def sumar(a: int, b: int):
    return {"resultado": suma(a, b)}
