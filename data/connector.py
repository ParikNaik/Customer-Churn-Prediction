import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

Customerdb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Deadlygamer905!",
      database="churn_database")

cursor = Customerdb.cursor()

cursor.execute("SELECT * FROM customerdata LIMIT 1;")

myresult = cursor.fetchone()

for x in myresult:
      print(x)



engine = create_engine("mysql://readonly_user:SecurePassword123!@localhost:3306/churn_database")

df = pd.read_sql("SELECT * FROM customerdata", engine)

#TODO: Create df as an object to be returned for use in preprocessing.py

cursor.close()

Customerdb.close()
