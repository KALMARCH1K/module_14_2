import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создание таблицы Users, если она ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Проверка на наличие данных в таблице
cursor.execute('''
SELECT COUNT(*) FROM Users
''')
data_exists = cursor.fetchone()[0]

# Если данных нет, заполняем таблицу 10 записями
if data_exists == 0:
    users_data = [
        ('User1', 'example1@gmail.com', 10, 1000),
        ('User2', 'example2@gmail.com', 20, 1000),
        ('User3', 'example3@gmail.com', 30, 1000),
        ('User4', 'example4@gmail.com', 40, 1000),
        ('User5', 'example5@gmail.com', 50, 1000),
        ('User6', 'example6@gmail.com', 60, 1000),
        ('User7', 'example7@gmail.com', 70, 1000),
        ('User8', 'example8@gmail.com', 80, 1000),
        ('User9', 'example9@gmail.com', 90, 1000),
        ('User10', 'example10@gmail.com', 100, 1000)
    ]

    cursor.executemany('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', users_data)

# Обновление balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute('''
UPDATE Users SET balance = 500 WHERE id % 2 = 1
''')

# Удаление каждой 3ей записи в таблице начиная с 1ой
cursor.execute('''
DELETE FROM Users WHERE id % 3 = 1
''')

# Удаление пользователя с id=6
cursor.execute('''
DELETE FROM Users WHERE id = 6
''')

# Подсчёт кол-ва всех пользователей
cursor.execute('''
SELECT COUNT(*) FROM Users
''')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('''
SELECT SUM(balance) FROM Users
''')
all_balances = cursor.fetchone()[0]


cursor.execute('''
SELECT username, email, age, balance FROM Users WHERE age != 60
''')


results = cursor.fetchall()


for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

average_balance = round(all_balances / total_users)
print(average_balance)
conn.commit()
conn.close()