from pydantic import BaseModel, EmailStr


class RegisRequest(BaseModel):
    full_name: str
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    username: str
