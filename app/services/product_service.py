import asyncpg
from fastapi.responses import JSONResponse
from app.core.jwt import create_jwt_token
from app.repo import UserRepo
from app.core.config import conf
from app.repo.product_repo import ProductRepo
from app.schemas import CreateProduct
from app.core.utils import hash_password, verify_password
from app.repo import product_repo


class ProductService:
    async def create_product(product_in: CreateProduct):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        ProductRepo.add_product(
            conn, product_in.name, product_in.price, product_in.stock_quantity
        )

    async def all_products():
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        await ProductRepo.all_products(conn)

