import pymysql

db = pymysql.connect("localhost", "root", "yoza", "perpusonair")
cursor = db.cursor()

query = "SELECT * from buku "
cursor.execute(query)
result = cursor.fetchall()

print result