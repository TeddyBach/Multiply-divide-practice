import mysql.connector, random, time
from config import  host, user, password
from datetime import datetime

name = input("What is your name? ")
table = int(input("What times table should we use? "))
reps = int(input("How many questions would you like to practice with? "))
count = 0
minutes_or_seconds = "seconds"

current_datetime = datetime.now()
start_time = time.time()

while True:
  for i in range(reps):
    possibilities = [" × ", " ÷ "]
    weights = [0.6667, 0.3333]
    random_sign = random.choices(possibilities, weights=weights, k=1)[0]
  
    if random_sign == " × ":
      trys = 1
  
      multiply_by = random.randint(1,12)
      place = random.randint(0,1)
      if place == 0:
        sol = table * multiply_by
        print(str(i + 1) + ". " + str(table) + " × " + str(multiply_by))
        while True:
          response = input("what is the answer? ")
          if int(response) != sol:
            print("Try again")
            trys += 1
          else:
            print("Correct!")
            break
        if trys == 1:
          count += 1
      elif place == 1:
        trys = 1
  
        sol = table * multiply_by
        print(str(i + 1) + ". " + str(multiply_by) + " × " + str(table))
        while True:
          response = input("what is the answer? ")
          if int(response) != sol:
            print("Try again")
            trys += 1
          else:
            print("Correct!")
            break
        if trys == 1:
          count += 1
    elif random_sign == " ÷ ":
      trys = 1
  
      divide_into = table * random.randint(1,12)
      sol = divide_into / table
      print(str(i + 1) + ". " + str(divide_into) + " ÷ " + str(table))
      while True:
        response = input("what is the answer? ")
        if int(response) != sol:
          print("Try again")
          trys += 1
        else:
          print("Correct!")
          break
      if trys == 1:
        count += 1
  
  end_time = time.time()
  time_spent = int(end_time - start_time)
  if time_spent >= 60:
    minutes_or_seconds = "minutes"
    print("Your score was", str(count), "out of", str(reps), "and spent", str(round(time_spent / 60, 2)), minutes_or_seconds)
  else:
    print("Your score was", str(count), "out of", str(reps), "and spent", str(time_spent), minutes_or_seconds)
  
  time_per_question = time_spent / reps
  
  time_per_question = time.strftime('%H:%M:%S', time.gmtime(time_per_question))
  time_spent = time.strftime('%H:%M:%S', time.gmtime(time_spent))
  
  #time_per_question_obj = time.strftime('%H:%M:%S', time_per_question_obj)

  #time_per_question = time.strptime(time_per_question, '%H:%M:%S')
  #print(time_per_question_obj,type(time_per_question_obj))
  #hours = time_per_question_obj // 3600
  #minutes = time_per_question_obj % 3600 // 60
  #seconds = time_per_question_obj % 60
  #time_per_question = f"{hours:02d}:{minutes:02d}:{seconds:02d}"


  #print(host, user, password)


  mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database="Multiply_divide_practice"
  )
  
  mycursor = mydb.cursor()
  #

  sql = "INSERT INTO Multiply_divide_practice (Date_completed, Number_correct, Total_number, Time_spent, Times_table, Time_per_question, name) VALUES (%s, %s, %s, %s, %s, %s, %s);"
  val = (current_datetime, count, reps, time_spent, table, time_per_question, name)
  mycursor.execute(sql, val)
  
  mydb.commit()
  
  print(mycursor.rowcount, "record inserted.")

  go_again = input("Would you like to go again? (y/n) ")
  count = 0
  if go_again == "n":
    break

