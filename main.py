from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return '<h1>hello fastapi</h1>'
    