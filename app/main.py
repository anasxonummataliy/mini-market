from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.repo import BaseRepo, OrderRepo
from app.core.config import conf


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await asyncpg.connect(
        f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
    )
    users = await OrderRepo.update_status(conn, 1, "confirmed")
    print(users)
    await BaseRepo.create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def run_app():
    return {"message": "Working"}
