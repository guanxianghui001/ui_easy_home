from fastapi import FastAPI
from uvicorn import run

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    # 运行fastapi程序
    run(app="main:app", host="127.0.0.1", port=8000, reload=True)
