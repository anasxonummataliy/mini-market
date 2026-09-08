from app.core.config import conf


class ProductRepo:
    @staticmethod
    async def add_product(conn, user_id, product_id, *, status):
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
    async def all_products(conn):
        products = conn.fetch("select * from products")
        return products
