import mysql.connector

d = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "God@1234",
    database = "mydatabase"
)

mycurser = d.cursor()

mycurser.execute("DELETE FROM customers WHERE name ='ABC' ")

d.commit()

'''
commit 

it is imp otherwise no change will be made to the table
'''

print(mycurser.rowcount, "record(s) deleted")