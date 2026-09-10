from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.repo import BaseRepo, OrderRepo, UserRepo
from app.core.config import conf


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await asyncpg.connect(
        f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
    )
    users = await UserRepo.add_user(conn, 'Oybek', 'anasxon1', '1234')
    print(users)
    await BaseRepo.create_tables(conn)
    await UserRepo.create_admin(conn)
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
