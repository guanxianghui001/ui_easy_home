from fastapi import FastAPI, HTTPException
from uvicorn import run
from app.schemas.project import *
from app.schemas.module import *
from app.common.response.response_schema import ResponseBase
from app.operation.project_operation import *
from app.operation.module_operation import *

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/ui/project/add", summary='增加项目')
async def add_project(item: AddProject):
    project_dict = item.dict()
    project_name = project_dict["project_name"].strip()
    if project_name == "":
        return response_base.fail(code=40002, msg='项目名称不能为空')
    else:
        datas = add_projects(project_name)
        if datas:
            return response_base.response_200(data={"id": datas[0], "project_name": datas[1]})
        else:
            return response_base.fail(code=40001, msg='存在相同的项目名')


@app.get("/ui/project/info", summary="查询项目数据")
async def get_project():
    datas = search_project()
    return response_base.response_200(data=datas)


@app.delete("/ui/project/delete", summary="删除项目")
async def delete_project(item: DeleteProject):
    project_dict = item.dict()
    datas = delete_projects(project_dict["project_name"])
    if datas:
        return response_base.response_200()
    else:
        return response_base.fail(code=40001, msg='项目已被删除或不存在')


@app.put("/ui/project/update", summary="删除项目")
async def update_project(item: UpdateProject):
    project_dict = item.dict()
    datas = update_projects(project_dict["id"], project_dict["project_name"])
    if datas:
        return response_base.response_200()
    else:
        return response_base.fail(code=40001, msg='项目已被删除或不存在')


@app.post("/ui/module/add", summary='增加项目')
async def add_module(item: AddModule):
    module_dict = item.dict()
    module_name = module_dict["name"].strip()
    if module_name == "":
        return response_base.fail(code=40002, msg='模块名称不能为空')
    else:
        module_dict["name"] = module_name
        datas = add_modules(module_dict)
        print(datas)
        if type(datas) == dict:
            return response_base.response_200(data=datas)
        else:
            return response_base.fail(code=datas[0], msg=datas[1])


@app.post("/ui/module/info", summary="查询模块数据")
async def get_module(item: SearchModule):
    project_data = dict(item)
    project_id = project_data["project_id"]
    datas = search_module(project_id)
    return response_base.response_200(data=datas)


@app.put("/ui/module/update", summary="删除项目")
async def update_module(item: UpdateModule):
    module_dict = item.dict()
    datas = update_modules(module_dict["id"], module_dict["module_name"])
    if datas:
        return response_base.response_200()
    else:
        return response_base.fail(code=40001, msg='模块已被删除或不存在')


response_base = ResponseBase()
if __name__ == '__main__':
    # 运行fastapi程序
    run(app="main:app", host="127.0.0.1", port=8000, reload=True)
