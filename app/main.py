from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.acupuncture_points import router as acupuncture_points_router

app = FastAPI()

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")


app = FastAPI()

app.include_router(acupuncture_points_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
