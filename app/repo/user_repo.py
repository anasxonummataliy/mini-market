from http.client import HTTPResponse
from urllib.error import HTTPError

from argon2 import verify_password
import asyncpg
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.core.config import conf
from app.core.jwt import create_jwt_token


class UserRepo:
    @staticmethod
    async def create_admin(conn):
        try:
            await conn.execute(
                "insert into users(full_name, username, password, role) values ('Admin', 'admin', 'admin' ,'admin')"
            )
        except:
            raise HTTPException(400, "Bu admin allaqachon yaratilgan.")

    @staticmethod
    async def add_user(conn, full_name, username, hash_password):
        try:
            found = await conn.execute(
                "select * from users where username = $1", username
            )
            if not found:
                raise HTTPException(
                    400, "Bunday foydalanuvchi mavjud boshqa username kiriting."
                )
            user = await conn.execute(
                "insert into users(full_name, username, password) values ($1, $2, $3) returning *",
                full_name,
                username,
                hash_password,
            )
            token = create_jwt_token(user.id)
            return JSONResponse(
                content={
                    "message": "Ro'yhatdan muvaffaqiyatli o'tildi.",
                    "token": token,
                }
            )
        except Exception as e:
            return HTTPException(400, f"Ro'yhatdan o'tishda xatolik. {e}")

    @staticmethod
    async def check_user(conn, username, password):
        try:
            user = await conn.fetch(
                "select * from users where username = $1", username
            )
            if verify_password(user.password, password):
                return user
            else:
                raise HTTPException(detail="Parol xato!", status_code=400)
        except:
            raise HTTPException(400, "Bunday user mavjud emas!")

