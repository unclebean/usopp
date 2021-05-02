import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from syrup.db import db
from syrup.models import User as ModelUser
from syrup.schema.user import User as SchemaUser
from syrup.config import settings
from syrup.jobs import execute_jobs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

# app.mount("/app", StaticFiles(directory=BASE_DIR+"/../kabuto/build/web"), name="app")


@app.on_event("startup")
async def startup():
    print(settings.app_name)
    await db.connect()
    await execute_jobs()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
def god_usopp():
    return "God Usopp"


@app.post("/user/")
async def create_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {"user_id": user_id}


@app.get("/user/{id}", response_model=SchemaUser)
async def get_user(id: int):
    user = await ModelUser.get(id)
    return SchemaUser(**user).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
