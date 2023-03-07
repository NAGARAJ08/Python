import mysql.connector

D = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "God@1234",
    database = "mydatabase"
)

mycurser = D.cursor()


# mycurser.execute("SHOW TABLES")

# for i in mycurser:
#     print(i)

mycurser.execute("SELECT * from customers WHERE address LIKE '%way%' ")

# mycurser.execute("SELECT * from customers WHERE address = 'Park Lane 38'")

for _ in mycurser:
    print(_)