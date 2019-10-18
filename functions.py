import math
import re
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="remotemysql.com", port=3306, username="ik1CmkEEXA", passwd="bOgm0Is8WA", database="ik1CmkEEXA")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS bmi (date DATETIME, height DOUBLE, weight DOUBLE, bmi DOUBLE)")
mycursor.execute("CREATE TABLE IF NOT EXISTS dist (date DATETIME, point1 VARCHAR(255), point2 VARCHAR(255), distance DOUBLE)")

def calculate_bmi(height, weight):
    if float(height) == 0:
        raise ZeroDivisionError("Height cannot be zero")
    metric_weight = float(weight) * 0.45
    metric_height = float(height) * 0.025
    height_squared = metric_height * metric_height
    bmi = metric_weight / height_squared
    rounded_bmi = round(bmi, 1)
    classification = ""
    if rounded_bmi < 18.5:
        classification = "Underweight"
    elif rounded_bmi >= 18.5 and rounded_bmi <= 24.9:
        classification = "Normal weight"
    elif rounded_bmi >= 25 and rounded_bmi <= 29.9:
        classification = "Overweight"
    elif rounded_bmi >= 30:
        classification = "Obese"
    final_arr = [str(rounded_bmi), classification]
    add_to_bmi(height, weight, final_arr)
    return final_arr

def shortest_distance(point1, point2):
    point1_separated = point1.split(",")
    point2_separated = point2.split(",")
    if len(point1_separated) != 2 or len(point2_separated) != 2:
        raise Exception("Wrong format")
    try:
        float(point1_separated[0])
        float(point2_separated[0])
        float(point1_separated[1])
        float(point2_separated[1])
    except ValueError:
        print("Value error")
    x_distance = (float(point1_separated[0]) - float(point2_separated[0])) * (float(point1_separated[0]) - float(point2_separated[0]))
    y_distance = (float(point1_separated[1]) - float(point2_separated[1])) * (float(point1_separated[1]) - float(point2_separated[1]))
    total_dist = round(math.sqrt(x_distance + y_distance), 2)
    add_to_dist(point1, point2, total_dist)
    return total_dist

def email_verifier(email):
    if email.count("@") != 1:
        return False
    username = email.split("@")[0]
    if username[0] == "." or username[len(username)-1] == ".":
        return False
    for i in range(len(username)):
        if username[i] == "." and username[i+1] == ".":
            return False
    if str.isdigit(username[0]):
        return False
    chars_not_allowed = ["(",")",",",":",";","<",">","@","[","]","\\","`"] # list of chars that can't be in email
    for i in username:
        if i in chars_not_allowed:
            return False
    return True

def split_bill(amount, guests):
    total_amount = float(amount) * 1.15
    divided_amount = total_amount / float(guests)
    num = int(guests)-1
    final_arr = [round(divided_amount,2)] * num
    final_num = total_amount - (divided_amount * float(num))
    final_arr.append(round(final_num,2))
    return final_arr

def add_to_bmi(height, weight, final_arr):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO bmi (date, height, weight, bmi) VALUES (%s, %s, %s, %s)"
    val = (dt_string, height, weight, final_arr[0])
    mycursor.execute(sql, val)
    mydb.commit()

def add_to_dist(point1, point2, distance):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO dist (date, point1, point2, distance) VALUES (%s, %s, %s, %s)"
    val = (dt_string, point1, point2, distance)
    mycursor.execute(sql, val)
    mydb.commit()

def print_bmi_list():
    mycursor.execute("SELECT * FROM bmi")
    myresult = mycursor.fetchall()
    print("\nBMI Entries:\nDate                | Height | Weight  | BMI ")
    for tuple in myresult:
        print(str(tuple[0]) + " | " + str(tuple[1]) + "   | " + str(tuple[2]) + "   | " + str(tuple[3]))

def print_dist_list():
    mycursor.execute("SELECT * FROM dist")
    myresult = mycursor.fetchall()
    print("\nDistance Entries:\nDate                | Point1 | Point2 | Distance")
    for tuple in myresult:
        print(str(tuple[0]) + " | " + str(tuple[1]) + "    | " + str(tuple[2]) + "    | " + str(tuple[3]))
