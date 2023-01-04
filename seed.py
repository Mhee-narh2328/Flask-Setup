import sqlite3

connection = sqlite3.connect('flask_tut.db' ,check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users (
        username,
        password,
        favourite_color
    )VALUES (
        'Muminat',
        'Adefabi',
        'pink'
    );"""
)

cursor.execute(
    """INSERT INTO users (
        username,
        password,
        favourite_color
    )VALUES (
        'Barakat',
        'Adefabi',
        'Gold'
    );"""
)

connection.commit()
cursor.close()
connection.close()