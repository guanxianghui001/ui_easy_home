from fastapi import FastAPI
import uvicorn
from routes.module import module_add

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/addmodule")
async def root():
    return module_add('hu')



if __name__ == '__main__':
    # 运行fastapi程序
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)