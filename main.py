from fastapi import FastAPI

app = FastAPI()


@app.get("/") # 路徑名稱
def read_root(): # 呼叫此function
    return {"Hello": "World"} # 執行function程式

@app.get("/happy") # 路徑名稱
def read_happy(): # 呼叫此function
    return "I am so happy." # 執行function程式