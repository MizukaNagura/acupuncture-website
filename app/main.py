from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.acupuncture_points import router as acupuncture_points_router
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # templatesディレクトリを設定

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# APIルーターのインクルード
app.include_router(acupuncture_points_router)

# ルートエンドポイント
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})