import mysql.connector

db = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "God@1234",
    database = "mydatabase"
)

mycusrsor = db.cursor()

sql = "INSERT INTO customers (name,address) VALUES (%s, %s)"
# val = ("ABC","Eng Alphabets")

# Inserting multiple records 
val = [

    ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
# mycusrsor.execute(sql,val) - 

# for many record we use executemany() method
# Here val is a list of tuples 
mycusrsor.executemany(sql,val)


db.commit()

print(mycusrsor.rowcount,"was inserted")
