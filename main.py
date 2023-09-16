from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


@app.get("/api/health")
async def health_check():
    return {"message": "Estou saudável 1"}


class FibonacciRequest(BaseModel):
    elementos: int

def calcular_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    return fibonacci


@app.post("/api/fibonacci", response_model=list[int])
async def fibonacci(request: FibonacciRequest):
    elementos = request.elementos
    if elementos < 0:
        raise HTTPException(status_code=400, detail="O número de elementos deve ser maior ou igual a 0")
    elif elementos == 0:
        return []
    elif elementos == 1:
        return [0]
    else:
        return calcular_fibonacci(elementos)
