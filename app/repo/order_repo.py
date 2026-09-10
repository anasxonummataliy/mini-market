from fastapi import HTTPException
from fastapi.responses import JSONResponse


class OrderRepo:
    @staticmethod
    async def add_order(conn, user_id, product_id, *, status):
        try:
            await conn.execute(
                "insert into orders(status, user_id, product_id) values ($1, $2, $3)",
                status,
                user_id,
                product_id,
            )
        except Exception as e:
            print(e)

    @staticmethod
    async def update_status(conn, order_id, status):
        try:
            order = await conn.fetch("select * from orders where id = $1;", order_id)
            if order:
                return HTTPException(
                    status_code=400, detail="Bunday order mavjud emas!"
                )
            await conn.execute(
                "update orders set status = $1 where id = $2;", status, order_id
            )
            return JSONResponse(
                content={
                    "message": "Order statusi o'zgartirildi.",
                }
            )
        except:
            return HTTPException(status_code=400, detail="Xatolik!")

    @staticmethod
    async def all_user_orders(conn, user_id):
        try:
            orders = await conn.fetch(
                "select * from orders where user_id = $1", user_id
            )
            return JSONResponse(content={"message": "", "orders": orders})
        except:
            return HTTPException(status_code=400, detail="Order mavjud emas")

    @staticmethod
    async def get_user_order(conn, user_id, order_id):
        try:
            order = await conn.fetch(
                "select * from orders where id = $1 and user_id = $2", order_id, user_id
            )
            return JSONResponse(content={"message": "", "order": order})
        except:
            return HTTPException(status_code=400, detail="Userning orderi mavjud emas")
