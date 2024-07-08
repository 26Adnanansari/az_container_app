from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World1", "World2": "Pakistan zinda bad 1234567 80"}
@app.get("/about")
def read_root():
    return {"Institue": "PIAIC", "Institue": "GIAIC"}

