from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель для POST-запросов
class RequestData(BaseModel):
    message: str

# Эндпоинт для GET-запросов
@app.get("/api")
def read_root():
    return {"message": "API is working"}

# Эндпоинт для POST-запросов
@app.post("/api/process")
def process_data(data: RequestData):
    response_message = f"Received: {data.message}"
    return {"response": response_message}

# Запуск сервера (для отладки)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
