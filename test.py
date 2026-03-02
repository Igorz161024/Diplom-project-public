import modules.db as db

db.test_connection()
db.drop_products_table()       # очистка старої таблиці
db.create_products_table()     # створення нової
db.insert_test_products()      # вставка тестових даних
db.fetch_products()            # вибірка і показ даних