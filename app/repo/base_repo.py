import asyncpg
from app.core.config import conf


class BaseRepo:
    @staticmethod
    async def create_tables(conn):
        try:
            await conn.fetch("create type user_role as enum('admin', 'user');")
        except:
            print("user enum yaratilgan")
        try:
            await conn.fetch(
                "create table users(id bigserial primary key , "
                "full_name varchar(255) not null, "
                "username varchar(255) not null unique, "
                "password varchar(255) not null, "
                "role user_role default 'user');"
            )
        except Exception as e:
            print(e)
        try:
            await conn.fetch(
                "create table products( \
                id  bigserial primary key, \
                name varchar(255) not null, \
                price numeric(10, 2) not null, \
                stock_quantity bigint not null)"
            )
        except Exception as e:
            print(e)

        try:
            await conn.fetch(
                "create type order_status as enum('pending', 'confirmed', 'cancelled');"
            )
        except Exception as e:
            print(e)
        try:
            await conn.fetch(
                "create table orders( \
                id bigserial primary key, \
                status order_status not null default 'pending', \
                user_id bigint, \
                product_id bigint, \
                foreign key(user_id) references users(id), \
                foreign key(product_id) references products(id))"
            )

        except Exception as e:
            print(e)
        await conn.close()
