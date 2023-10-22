from fastapi import FastAPI

api  = FastAPI()

@api.get("/")
def get_root():
    return {'message': "Hello World"}


@api.post("/")
def get_post():
    return {'message': "Hello World do post!"}


@api.get("/novo_endpoint")
def get_root():
    return {'message': "Parabéns você criou um novo endpoint"}
