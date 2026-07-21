from db import get_db

connection = get_db()

if connection.is_connected():
    print("Connected Successfully!")

connection.close()