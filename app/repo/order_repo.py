from app.core.config import conf


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
            await conn.execute(
                "update orders set status = $1 where id = $2;", status, order_id
            )
        except Exception as e:
            print(e)

    @staticmethod
    async def all_orders(conn, user_id):
        orders = conn.fetch("select * from orders where id = $1", user_id)
        return orders

    @staticmethod
    async def get_orders(conn, user_id):
        orders = conn.fetch("select * from orders where id = $1", user_id)
        return orders
