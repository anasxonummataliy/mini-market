from fastapi import HTTPException
from fastapi.responses import JSONResponse


class ProductRepo:
    @staticmethod
    async def add_product(conn, name, price, stock_quantity):
        try:
            product = await conn.fetch(
                "insert into products(name, price, stock_quantity) values ($1, $2, $3) returning *",
                name,
                price,
                stock_quantity,
            )
            return JSONResponse(
                content={"message": "Product yaratildi.", "product": product}
            )
        except Exception as e:
            return HTTPException(status_code=400, detail="Product yaratishda xatolik!")

    @staticmethod
    async def all_products(conn):
        try:
            products = conn.fetch("select * from products")
            return JSONResponse(
                content={"message": "Product yaratildi.", "products": products}
            )
        except:
            return HTTPException(status_code=400, detail="Product mavjud emas!")
