from fastapi import FastAPI
from uvicorn import run
from app.schemas.project import AddProject
from app.common.response.response_schema import ResponseBase, ResponseModel
from app.operation.project_operation import add_project

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/ui/add/project/", summary='增加项目', response_model=ResponseBase)
async def add_projects(item: AddProject):
    project_dict = item.dict()
    try:
        add_project(project_dict["project_name"])
        print(ResponseBase.success())
        return ResponseBase.success()
    except Exception as e:
        print(e)
        return ResponseBase.fail()


if __name__ == '__main__':
    # 运行fastapi程序
    run(app="main:app", host="127.0.0.1", port=8000, reload=True)
