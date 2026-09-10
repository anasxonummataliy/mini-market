from pydantic import BaseModel, EmailStr

class CreateProduct(BaseModel):
    name: str
    price: float
    stock_quantity: int
