import sqlite3
conn = sqlite3.connect('hw.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_title TEXT NOT NULL,
                   price REAL NOT NULL DEFAULT 0.0,
                   quantity INTEGER NOT NULL DEFAULT 0)''')
def add_products():
    products = [("Мыло", 45.0, 10),
                ("Детское мыло", 35.0, 20),
                ("Одноразовые тарелки", 75.0, 5),
                ("Одноразовые ложки", 40.0, 15),
                ("Одноразовые кружки", 55.0, 10),
                ("Одноразовые вилки", 30.0, 25),
                ("Мороженое с ванильным вкусом", 65.0, 8),
                ("Мороженое с шоколадным вкусом", 65.0, 12),
                ("Мороженое с клубничным вкусом", 65.0, 6),
                ("Мороженое с карамельным вкусом", 65.0, 9),
                ("Мороженое с фисташковым вкусом", 65.0, 15),
                ("Мороженое с ореховым вкусом", 65.0, 11),
                ("Мороженое с кокосовым вкусом", 65.0, 7),
                ("Мороженое с фруктовым вкусом", 65.0, 14),
                ("Мороженое с мятным вкусом", 65.0, 10)]
    cursor.executemany(f"INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    print(f"Добавлено 15 товаров в БД.")

def change_quantity_by_id(id, quantity):
    cursor.execute(f"UPDATE products SET quantity = ? WHERE id = ?", (quantity, id))
    conn.commit()
    print(f" Количество товара с id {id} изменено на {quantity}.")

def change_price_by_id(id, price):
    cursor.execute(f"UPDATE products SET price = ? WHERE id = ?", (price, id))
    conn.commit()
    print(f"Цена товара с id {id}  изменена на {price} сомов.")

def delete_product_by_id(id):
    cursor.execute(f"DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    print(f"Удален товар с id {id} из БД.")
def select_all_products():
    cursor.execute(f"SELECT * FROM products")
    print(f"Товары в БД:")
    for row in cursor.fetchall():
        print(row)
def select_products_by_price_and_quantity():
    cursor.execute(f"SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
    print(f"Товары дешевле 100 сомов и количество которых больше 5:")
    for row in cursor.fetchall():
        print(row)

def search_products_by_title(title):
    cursor.execute(f"SELECT * FROM products WHERE product_title LIKE ?", (f'%{title}%',))
    print(f"Результаты поиска для '{title}':")
    for row in cursor.fetchall():
        print(row)

add_products()
change_quantity_by_id(2, 25)

change_price_by_id(4, 50.0)

delete_product_by_id(5)

select_all_products()

select_products_by_price_and_quantity()

search_products_by_title("мыло")

conn.close()