import mysql.connector

customerDB = mysql.connector.connect(host="localhost",user="root", passwd="Deadlygamer905!", database = "churn_database")

cursor = customerDB.cursor()

cursor.execute("describe customer")

for i in cursor:
    print(i)