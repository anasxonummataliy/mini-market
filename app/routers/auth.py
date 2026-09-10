from fastapi import APIRouter, Depends, HTTPException

from app.schemas.auth import LoginRequest, RegisRequest, UserResponse
from app.services.user_service import UserService

auth_router = APIRouter(prefix="/auth")


async def get_user_service():
    return UserService()


@auth_router.post("/register")
async def register(
    user_in: RegisRequest, user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    try:
        user_service.create_user(user_in)
    except Exception as e:
        return HTTPException(f"Ro'yhatdan o'tishda xatolik: {e}")


@auth_router.post('/login')
async def login(user_in: LoginRequest, user_service: UserService = Depends(get_user_service)):
    try:
        user_service.user_login(user_in)
    except:
        return HTTPException(status_code=400, detail='Login qilishda xatolik!')


