from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def hello_world():
    return "hola semillero"

@app.get("/hello2")
def hello_world_2():
    return "hola semillero 2"

handler = Mangum(app)
