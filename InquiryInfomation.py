def InfoPrint(all_info, var1, j):
    if var1 == 1:
        name = all_info[0].split(";")[0]
        idd = all_info[0].split(";")[1]
        dob = all_info[0].split(";")[2]
        mobile = all_info[0].split(";")[3]
        cl = [''] * j
        cm = [''] * j
        year = [''] * j
        d1 = [''] * j
        d2 = [''] * j
        rb = 0

        for i in range(0, j):
            cl[i] = all_info[i].split(";")[4]
            cm[i] = all_info[i].split(";")[5]
            year[i] = all_info[i].split(";")[6]
            d1[i] = all_info[i].split(";")[7]
            d2[i] = all_info[i].split(";")[8]
            rb = rb + int(all_info[i].split(";")[9])

        print("The Name is : " + name)
        print("The ID is : " + idd)
        print("The Birthday is : " + dob)
        print("The Mobile number is " + mobile)
        print("The Cars Rented By " + name + " :\n")
        for i in range(0, j):
            print("   The car license of the car number" + str(i + 1) + " is : " + cl[i] + " | The Name & Model is : " +
                  cm[
                      i] + " " + year[i]
                  + " | Rented this Car from " + d1[i] + " to " + d2[i])
        print("\nThe Total Money paid by " + name + " = " + str(rb))

    elif var1 == 2:

        cl = all_info[0].split(";")[4]
        cm = all_info[0].split(";")[5]
        year = all_info[0].split(";")[6]
        name = [''] * j
        idd = [''] * j
        mobile = [''] * j
        d1 = [''] * j
        d2 = [''] * j
        rb = 0

        for i in range(0, j):
            name[i] = all_info[i].split(";")[0]
            idd[i] = all_info[i].split(";")[1]
            mobile[i] = all_info[i].split(";")[3]
            d1[i] = all_info[i].split(";")[7]
            d2[i] = all_info[i].split(";")[8]
            rb = rb + int(all_info[i].split(";")[9])

        print("\nThe Car Licence number : " + cl)
        print("The Car Name : " + cm)
        print("Model : " + year)
        print("This Cars Rented By : \n")
        for i in range(0, j):
            print(
                str(i + 1) + " - " + name[i] + " | ID : " + idd[i] + " | Mobile : " + mobile[i] + " | Rented this Car "
                                                                                                  "from " + d1[
                    i] + " to " + d2[i])
        print("\n\nThe Total Revenue by Rented this car = " + str(rb))


def NameId(the_search):

    var = 1
    name_of_file = "CarRentalCompleted.txt"
    fo = open(name_of_file, "r")  # open the spesific file
    count = len(fo.readlines())  # get the length of file
    fo.close()  # close the file ( here i open the file just for know the length)
    car_info = [''] * count  # Initialize the list to add all the car Info to it
    ii = 0  # index connecting with previous list
    with open(name_of_file, "r") as file:  # open a file to read the lines ( line by line )
        s = file.readlines()
        for i in range(0, count):
            if the_search == s[i].split(";")[0] or the_search == s[i].split(";")[1]:
                car_info[ii] = s[i]
                ii += 1
            else:
                continue

    car_info[:] = [item for item in car_info if item != '']
    InfoPrint(car_info, var, ii)
    return


def CL(the_search):
    var = 2
    name_of_file = "CarRentalCompleted.txt"
    fo = open(name_of_file, "r")  # open the spesific file
    count = len(fo.readlines())  # get the length of file
    fo.close()  # close the file ( here i open the file just for know the length)
    car_info = [''] * count  # Initialize the list to add all the car Info to it
    ii = 0  # index connecting with previous list
    with open(name_of_file, "r") as file:  # open a file to read the lines ( line by line )
        s = file.readlines()
        for i in range(0, count):
            if the_search == s[i].split(";")[4]:
                car_info[ii] = s[i]
                ii += 1
            else:
                continue

    car_info[:] = [item for item in car_info if item != '']
    InfoPrint(car_info, var, ii)
    return


def Start():

    print ("\n***** Welcome to the  Information Center *****\n")
    print(" Please Select One Of The Following : \n "
          " 1 - Inquiry about a person using the NAME or ID .\n "
          " 2 - Inquiry about a car using the CL. ")
    x = input(" Press Here  [1/2] : ")
    while int(x) not in range(1, 3):
        print(" Not Valid Input ")
        x = input(" Press Here  [1/2] : ")

    try:
        if int(x) == 1:
            cho = input("\nEnter the name or id of the person : ")
            NameId(cho)
            print("\nThank you !!!\n")
            x = input(" press [1] for back to the main menu  ")
            while int(x) not in range(1, 2):
                print(" not valid input ")
                x = input(" press [1] for back to the main menu  ")
            if int(x) == 1:
                return

        else:
            cho = input("\nEnter the license Car Number : ")
            CL(cho)
            print("\nThank you !!!\n")
            x = input(" press [1] for back to the main menu  ")
            while int(x) not in range(1, 2):
                print(" not valid input ")
                x = input(" press [1] for back to the main menu  ")
            if int(x) == 1:
                return


    except:
        print(" \nSomething Error .. May be the Information that you Entered \n")
        print(" TO Try Again press 1\n"
              " TO Return To The Main Menu press 2")
        z = input(" Press Here : ")
        while int(z) not in range(1, 3):
            print(" Not Valid Input ")
            z = input(" Press Here : ")
        if int(z) == 1:
            Start()
        else:
            return
