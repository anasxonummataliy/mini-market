import asyncpg
from app.core.config import conf


class BaseRepo:
    @staticmethod
    async def create_tables():
        conn = await asyncpg.connect(
            f"postgresql://{conf.PG_USER}:{conf.PG_PASSWORD}@{conf.PG_HOST}:{conf.PG_PORT}/{conf.PG_DB}"
        )
        try:
            await conn.fetch(
                "create table users(id bigserial primary key , "
                "full_name varchar(255), "
                "username varchar(255), "
                "password varchar(255))"
            )
        except Exception as e:
            print(e)
        try:
            await conn.fetch(
                "create table products( \
                id  bigserial primary key, \
                name  varchar(255)   not null, \
                price  numeric(10, 2) not null, \
                stock_quantity bigint)"
            )
        except Exception as e:
            print(e)

        try:
            await conn.fetch(
                "create type order_status as enum('pending', 'confirmed', 'cancelled');"
            )
            await conn.fetch("create table orders( \
                id     bigserial primary key, \
                status order_status not null default 'pending', \
                user_id    bigint, \
                product_id bigint, \
                foreign key(user_id) references users(id), \
                foreign key(product_id) references products(id))")

        except Exception as e:
            print(e)
        await conn.close()
