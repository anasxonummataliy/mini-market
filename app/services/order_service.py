import asyncpg
from fastapi.responses import JSONResponse

from app.core.config import conf
from app.repo import OrderRepo
from app.schemas import CreateOrder


class OrderService:
    async def create_order(order_in: CreateOrder):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        OrderRepo.add_order(
            conn, order_in.name, order_in.price, order_in.stock_quantity
        )

    async def user_all_orders(user_id):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        await OrderRepo.all_user_orders(conn, user_id)

    async def user_order(user_id, order_id):
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        await OrderRepo.get_user_order(conn, user_id, order_id)
