import mysql.connector

DataB = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "God@1234",
    database = "mydatabase"
)

mycurser = DataB.cursor()

# mycurser.execute("DROP TABLE info")


mycurser.execute("SHOW DATABASES")
for i in mycurser:
    print(i)
