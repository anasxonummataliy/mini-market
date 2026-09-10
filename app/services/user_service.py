import asyncpg
from fastapi.responses import JSONResponse
from app.core.jwt import create_jwt_token
from app.repo import UserRepo
from app.core.config import conf
from app.schemas import RegisRequest
from app.core.utils import hash_password, verify_password
from app.schemas.auth import LoginRequest


class UserService:
    async def create_user(user_in: RegisRequest):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        password_hash = hash_password(user_in.password)
        UserRepo.add_user(
            conn, user_in.full_name, user_in.username, password_hash
        )

    async def login_user(user_in: LoginRequest):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        user = UserRepo.check_user(conn, user_in)
        if user:
            token = create_jwt_token(user.id)
            return JSONResponse(
                content={
                    "message": "Siz muvafaqiyatli login qildingiz.",
                    "token": token,
                },
            )
