import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Chadanishahi2001@gmail.com",
        database="todo_app",
        port=3306,
    )
    print("Connected successfully!")
    conn.close()

except Exception as e:
    print(e)