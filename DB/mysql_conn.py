import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="God@1234",
  database="mydatabase"

)

# curser is an object that is used to make the connection for executing SQL queries

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")

# for i in mycursor:
#     print(i)


# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for i in mycursor:
#     print(i)

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("DESCRIBE customers")

mycursor.execute("SELECT * FROM customers")




# fetchall() it fetches all(remaining rows of the query result )
for i in mycursor.fetchall():
    print(i)