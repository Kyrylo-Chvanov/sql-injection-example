import re
import sqlite3


connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users(username, password)")
cursor.execute(
    """
    INSERT INTO users VALUES
        ('Diego', '123'),
        ('Sergio', 'password'),
        ('Kyrylo', 'pepe')
    """
)

VALID_INPUT = re.compile(r"^[A-Za-z0-9_.@\-]{1,64}$")

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not VALID_INPUT.fullmatch(username) or not VALID_INPUT.fullmatch(password):
        print("Invalid input")
        continue

    cursor.execute(
        """
        SELECT username
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password),
    )

    if cursor.fetchone() is None:
        print("Access denied")
    else:
        print("Access granted")
