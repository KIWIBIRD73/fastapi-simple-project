import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/', tags=['Greeting'], summary="Получить привет от сервера")
def get_hello():
    return {"message": "Hello from FastApi!"}


if __name__ == '__main__':
    """
    Для запуска через uvicorn необходимо указать путь до основного объекта приложения FastApi

    src - папка, в котрой лежит main фаил
    main - имя файла (main.py)
    app - объект приложения FastApi()

    Путь до файла указывать через точку, путь до объекта FastApi() указывать через двоеточие
    """
    uvicorn.run('main:app', reload=True)
