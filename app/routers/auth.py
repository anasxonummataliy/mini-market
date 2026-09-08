from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')

@auth_router('/register')
async def register():
    pass


