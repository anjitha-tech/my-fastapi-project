from fastapi import FastAPI

# Create app
app = FastAPI()

# First route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Second route
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# Third route - POST example
@app.post("/items")
def create_item(name: str, price: float):
    return {"item_name": name, "price": price}