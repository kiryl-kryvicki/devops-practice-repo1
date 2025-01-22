#Api
static_string = "Initial text"

from fastapi import FastAPI
app = FastAPI()
@app.get("/get-message")
async def read_root():
    return {"Message": "Congrats! This is your first API!"}

@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return {"message": "Text added", "current_string": static_string}

@app.put("/change")
async def change_text(new_text: str):
    global static_string
    static_string = new_text
    return {"message": "Text changed", "current_string": static_string}

@app.delete("/remove")
async def remove_text():
    global static_string
    static_string = ""
    return {"message": "Text removed"}