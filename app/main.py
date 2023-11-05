from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.acupuncture_points import router as acupuncture_points_router

app = FastAPI()

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# APIルーターのインクルード
app.include_router(acupuncture_points_router)

# ルートエンドポイント
@app.get("/")
async def root():
    return {"message": "Hello World"}
