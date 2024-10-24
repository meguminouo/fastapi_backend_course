from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str # 必填
    price: float
    description: str =None # 非必填

@app.get("/") # 路徑名稱
def read_root(): # 呼叫此function
    return {"Hello": "World"} # 執行function程式

@app.get("/happy") # 路徑名稱
def read_happy(): # 呼叫此function
    return "I am so happy." # 執行function程式

@app.get("/items/") # 路徑名稱
def creat_item(item: Item): # 呼叫此function
    print(f"Recive item: {item}")
    return {"message": "Item recived" ,"item": item} # 執行function程式
