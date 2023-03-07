import mysql.connector

DataB = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "God@1234",
    database = "mydatabase"
)

mycurser = DataB.cursor()

mycurser.execute("SELECT * FROM customers ORDER BY name DESC") # it gives ascending order by default

for _ in mycurser:
    print(_)
