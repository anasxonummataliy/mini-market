from pydantic import BaseModel, EmailStr


class CreateOrder(BaseModel):
    status: str
    user_id: int
    product_id: int
