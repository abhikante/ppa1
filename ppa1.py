from functions import *

print("Welcome to the app! Choose a function to use or press 9 to quit:")
prev_value = 0
while 1 == 1:
    option = input("1: Calculate BMI   2: Shortest Distance Between 2 Points   3: Email Verifier    4: Bill Split Calculator    9: Quit\n")
    if prev_value != option:
        print_bmi_list()
        print_dist_list()
    print()
    prev_value = option
    if int(option) == 1:
        height = input("Enter height in inches: ")
        weight = input("Enter weight in pounds: ")
        try:
            float(height)
            float(weight)
        except ValueError:
            print("Input has to be a number")
            continue
        if float(height) == 0:
            print("Height cannot be 0")
            continue
        bmi_info = calculate_bmi(height, weight)
        print("Your BMI is " + bmi_info[0] + " and you fall under the " + bmi_info[1] + " category.")
    elif int(option) == 2:
        point1 = input("Enter point 1 as 2 coordinates separated by a comma (x1,y1): ")
        point2 = input("Enter point 2 in the same format: ")
        if len(point1.split(",")) != 2 or len(point2.split(",")) != 2:
            raise Exception("Wrong format! Please try again with the correct format")
            continue
        try:
            float(point1.split(",")[0])
            float(point2.split(",")[0])
            float(point1.split(",")[1])
            float(point2.split(",")[1])
        except ValueError:
            print("You didn't input a number somewhere! Please try again")
            continue
        dist = shortest_distance(point1, point2)
        print("The shortest distance between these two points is: " + str(dist))
    elif int(option) == 3:
        email = input("Enter an email and we'll verify if it follows all requirements: ")
        if email_verifier(email) == True:
            print("This email follows all requirements!")
        else:
            print("Unfortunately, this email does not follow all requirements")
    elif int(option) == 4:
        amount = input("Enter bill's total amount without tip: ")
        guests = input("Enter total number of guests: ")
        final_arr = split_bill(amount, guests)
        for i in range(len(final_arr)):
            print("Guest " + str(i+1) + " owes: " + str(final_arr[i]))
    elif int(option) == 9:
        print("Thanks for using the app, goodbye!")
        mycursor.execute("SELECT * FROM bmi")
        myresult = mycursor.fetchall()
        print("Previous BMI Values:\n")
        for x in myresult:
            print(x)
        mycursor.execute("SELECT * FROM dist")
        myresult = mycursor.fetchall()
        print("Previous Distance Values:\n")
        for x in myresult:
            print(x)
        break
    print("\nChoose a new function")
