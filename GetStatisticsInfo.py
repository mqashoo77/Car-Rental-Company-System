from datetime import *


def LineOfFile(file_name):
    file1 = open(file_name, "r")

    count = len(file1.readlines())
    file1.close()
    return count


def CalcDays(x, y):  # Function to return the Number of days between two dates
    d1 = x
    d1 = datetime.strptime(d1, '%d %B %Y')  # change the pprivious formate of date that incluse in files  +
    d1 = d1.strftime('%Y-%m-%d')  # + To this formate (YYYY-MM-DD)
    d1 = d1.split("-")
    d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))  # change to number stile to sub from another date

    d2 = y
    d2 = datetime.strptime(d2, '%d %B %Y')
    d2 = d2.strftime('%Y-%m-%d')
    d2 = d2.split("-")
    d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
    # print(d1)
    # print(d2)

    z = (d2 - d1).days  # sub the two date to get the days that wanted

    return z  # return the number


def NumberOfDays(nof, l, number_of_line):
    date11 = l.split(";")[7]
    date12 = l.split(";")[8]
    total_days = CalcDays(date11, date12)
    count = LineOfFile(nof)
    file_for_reading = open(nof, "r")
    read = file_for_reading.readlines()
    for i in range(0, count):
        if i == number_of_line:
            continue
        elif l.split(";")[4] == read[i].split(";")[4]:
            date21 = read[i].split(";")[7]
            date22 = read[i].split(";")[8]
            days_for_this_two_dates = CalcDays(date21, date22)
            total_days = total_days + days_for_this_two_dates
        else:
            continue
    file_for_reading.close()
    return total_days


def RevenueByCar(nof, l, nol):
    revenue1 = l.split(";")[9]
    total_revenue = int(revenue1)
    count = LineOfFile(nof)
    file_for_reading = open(nof, "r")
    read = file_for_reading.readlines()
    for i in range(0, count):
        if i == nol:
            continue
        elif l.split(";")[4] == read[i].split(";")[4]:
            revenue2 = read[i].split(";")[9]
            total_revenue = total_revenue + int(revenue2)
        else:
            continue
    file_for_reading.close()
    return total_revenue


def PrintInfoCars(v):
    print(" How I can Help You ? \n")
    print(" 1- Get Information about Number of Days for renting each car. \n"
          " 1- Get Information about Revenue for renting each car.\n"
          " 3- Get Information about Average price per day for renting each car.\n"
          " 4- Get Get Information about All previous Things ")
    y = input(" Press Here :  ")
    while int(y) not in range(1, 5):
        print(" Not Valid Input ")
        y = input(" Press Here : ")

    if int(y) == 1:
        for i in range(0, len(v)):
            car = v[i]
            car = car.split(";")
            print(" The car number " + str(i) + " is : " + car[1] + " | Model : " + car[
                2] + "| The car license number is : " + car[0] + "|" + " The Total days rented this car is : " +
                  car[3])

    elif int(y) == 2:
        for i in range(0, len(v)):
            car = v[i]
            car = car.split(";")
            avg_price = int(car[4]) // int(car[3])
            print(" The car number " + str(i + 1) + " is : " + car[1] + " | Model : " + car[
                2] + "| The car license number is : " + car[0] + "|" + " The Revenue made by renting this car =  " +
                  car[4])
    elif int(y) == 3:
        for i in range(0, len(v)):
            car = v[i]
            car = car.split(";")
            avg_price = int(car[4]) // int(car[3])
            print(" The car number " + str(i + 1) + " is : " + car[1] + " | Model : " + car[2] +
                  "| The car license number is : " + car[
                      0] + "|" + " The Average price for renting this car = " + str(avg_price))

    else:
        for i in range(0, len(v)):
            car = v[i]
            car = car.split(";")
            avg_price = int(car[4]) // int(car[3])
            print(" The car number " + str(i + 1) + " is : " + car[1] + " | Model : " + car[2] +
                  "| The car license number is : " + car[0] + "|" + " The Total days rented this car is : " + car[3] +
                  "|  The Revenue made by renting this car = " + car[
                      4] + " | The Average price for renting this car = " + str(avg_price))

    print("\n Thank You \n ")

    return


def Start():
    print(" * Welcome to Cars Rented Statistics Center \n")  # Welcom messege
    x = input(" * To Continue press [1] : ")
    while int(x) not in range(1, 2):  # Get the feedback from user with limiting acces
        print(" Not Valid Input ")  # if the user doesnt press 1 to continue this messege will out
        x = input(" * To Continue press [1] : ")  # lopp until user print the true value to cont>>

    name_of_file = "CarRentalCompleted.txt"
    fo = open(name_of_file, "r")  # open the spesific file
    count = len(fo.readlines())  # get the length of file
    fo.close()  # close the file ( here i open the file just for know the length)

    if int(x) == 1:  # user choice  to continue

        cars = [''] * count  # Initialize the list to add all the car Info to it
        cars_cl = [''] * count  # Initialize the list to add all the cl of all the car to make  use it in if  after for

        ii = 0  # index connecting with previous two list

        with open(name_of_file, "r") as file:  # open a file to read the lines ( line by line )
            s = file.readlines()
            for i in range(0, count):  # loop for get the information that wanted according to i Line
                if s[i].split(";")[4] in cars_cl:  # check if this car is readied or not
                    continue  # if the car is Readied before continue in the loop to get another car
                else:
                    cars[ii] = s[i].split(";")[4] + ";" + s[i].split(";")[5] + ";" + s[i].split(";")[
                        6]  # get the cl & cm & year of car
                    number_of_day = NumberOfDays(name_of_file, s[i], i)  # calclute all days of rental this car
                    revenue_by_car = RevenueByCar(name_of_file, s[i], i)
                    # calclute all revenue price for rental this car

                    cars_cl.insert(ii, s[i].split(";")[4])
                    cars[ii] = cars[ii] + ";" + str(number_of_day) + ";" + str(revenue_by_car)
                    # plus the days and revenue info to car information

                    ii += 1

        cars[:] = [item for item in cars if item != '']  # remove all element that contain nothing in cars list

        file.close()
        PrintInfoCars(cars)  # Function that ptint the wanted info as the user want

        x = input(" press [1] for back to the main menu  ")
        while int(x) not in range(1, 2):
            print(" not valid input ")
            x = input(" press [1] for back to the main menu  ")
        if int(x) == 1:
           return
        else:
            exit()
    else:
        exit()
