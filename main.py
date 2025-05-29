from fastapi import FastAPI

app = FastAPI()

@app.get("/") # This is how we defined a path. Path in this case is the "/"
def root():
    return {"Hello" : "World"}