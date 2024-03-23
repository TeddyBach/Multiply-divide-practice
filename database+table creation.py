import mysql.connector
from config import user, password



mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  password=password
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Multiply_divide_practice")


mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  password=password,
  database="Multiply_divide_practice"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Multiply_divide_practice (id INT AUTO_INCREMENT PRIMARY KEY, Date_completed datetime, Number_correct integer, Total_number integer, Time_spent time, Times_table integer, Time_per_question time)")

