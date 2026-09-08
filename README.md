# mini-market


1. Dastur FastAPI va databasedan Postgresql va asyncpg dan foydalanilmoqda.
2. asycnpg asosida user, product va category(database/models.py) ichida yaratildi.
3. order modeli (user_id, product_id, status(pending, confirmed, cancelled))
4. 15 minut ichida tolamasa buyurtma bekor qilinsin

User model
-- id
-- full_name
-- username
-- password

Product model
-- id
-- name
-- price
-- stock_quantity

Order model
-- id
-- user_id
-- product_id
-- status


