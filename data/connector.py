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

    # Fetch all rows
myresult = cursor.fetchone()

    # Iterate and print the data
for x in myresult:
      print(x)


#TODO: Create an object to contain data from table thatll be used in the preprocessing.py file

engine = create_engine("mysql://readonly_user:SecurePassword123!@localhost:3306/churn_database")
df = pd.read_sql("SELECT * FROM customerdata", engine)
print(df.head())


cursor.close()

Customerdb.close()
