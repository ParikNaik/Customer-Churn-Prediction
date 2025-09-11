import mysql.connector

Customerdb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Deadlygamer905!",
      database="churn_database")

cursor = Customerdb.cursor()

cursor.execute("SELECT * FROM customerdata LIMIT 1;")

    # Fetch all rows
myresult = cursor.fetchone()

    # Iterate and print the data
for x in myresult:
      print(x)

cursor.close()

Customerdb.close()
