import math
import re

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
    return round(math.sqrt(x_distance + y_distance), 2)

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
