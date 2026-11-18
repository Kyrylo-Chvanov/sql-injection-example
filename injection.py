import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("CREATE TABLE users(username, password)")
cursor.execute("""
    INSERT INTO users VALUES
        ('Diego', '123'),
        ('Sergio', 'password'),
        ('Kyrylo', 'pepe')
""")

while True:
    username = input("Username: ")
    password = input("Password: ")

    res = cursor.execute(f"""
        SELECT username
        FROM users
        WHERE username = '{username}'
        AND password = '{password}'                         
    """)

    if res.fetchone() is None:
        print("Access denied")
    else:
        print("Access granted")
