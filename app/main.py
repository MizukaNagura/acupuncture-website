from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.acupuncture_points import router as acupuncture_points_router
from fastapi.templating import Jinja2Templates
from fastapi import Request
from .schemas import Item

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # templatesディレクトリを設定

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# APIルーターのインクルード
app.include_router(acupuncture_points_router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/")
async def read_items():
    return {"message": "GETリクエストに対するレスポンス"}

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "POSTリクエストによってアイテムが作成されました", "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"message": "PUTリクエストによってアイテムが更新されました", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "DELETEリクエストによってアイテムが削除されました", "item_id": item_id}
