from modules.db import create_users_table, drop_users_table, fetch_users
from modules.users import User
from modules.products import Product

def main():
    print('Diplom Project ERP-система запущена')

    # 1. Створюємо таблицю users
    drop_users_table()
    create_users_table()

    # 2. Створюємо користувачів
    user1 = User('admin', 'superuser')
    user2 = User('manager', 'staff')
    print(user1)
    print(user2)

    # 3. Вибірка всіх користувачів
    print("Список користувачів у базі:")
    fetch_users()

    # 4. Оновлення користувача
    user1.update(user_id=1, role='manager')

    # 5. Видалення користувача
    user2.delete(user_id=2)

    # 6. Створюємо продукт
    product = Product('Laptop', 25000, 10)
    print(product)

if __name__ == '__main__':
    main()
