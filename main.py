from fastapi import FastAPI
from uvicorn import run
from app.schemas.project import AddProject
from app.common.response.response_schema import ResponseBase
from app.operation.project_operation import *

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/ui/add/project", summary='增加项目')
async def add_projects(item: AddProject):
    project_dict = item.dict()
    try:
        datas = add_project(project_dict["project_name"])
        if datas:
            return response_base.response_200(data={"id": datas[0], "project_name": datas[1]})
        else:
            return response_base.fail(code=40001,msg='存在相同的项目名')

    except Exception as e:
        print(e)
        return response_base.fail()


@app.get("/ui/project/info", summary="查询项目数据")
async def get_project():
    try:
        datas = search_project()
        return response_base.response_200(data=datas)
    except Exception as e:
        print(e)
        return response_base.fail()


response_base = ResponseBase()
if __name__ == '__main__':
    # 运行fastapi程序
    run(app="main:app", host="127.0.0.1", port=8000, reload=True)
