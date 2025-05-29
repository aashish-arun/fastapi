from fastapi import FastAPI

app = FastAPI()

items = [] # Have to keep in mind that this is ran every time we make a change to the project and it reloads. i.e. we also have to add item every time we change this file so that we can use the other methods on it

@app.get("/") # This is how we defined a path. Path in this case is the "/"
def root():
    return {"Hello" : "World"}

@app.post("/items") 
def create_item(item:str): # This is the cmd used instead of curl in windows for post requests "Invoke-WebRequest -Uri "http://localhost:8000/items?item=item_name" -Method POST"
    items.append(item)
    return items

@app.get("/items/{item_id}") 
def get_item(item_id:int) -> str: # This is the cmd used instead of curl in windows for get requests "Invoke-WebRequest -Uri "http://localhost:8000/items/item_id""
    item = items[item_id]
    return item