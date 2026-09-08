from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')

@auth_router()
async def register():
    pass

# register qilish
# login qildim
