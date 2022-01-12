from datetime import *


def LineOfFile(file_name):
    file1 = open(file_name, "r")

    count = len(file1.readlines())
    file1.close()
    return count


def FormatDate(pfd):
    pfd = str(pfd)
    if '-' in pfd:
        pfd = datetime.strptime(pfd, '%Y-%m-%d')
        nfd = pfd.strftime('%d %B %Y')
        nfd = str(nfd)
        return nfd
    elif '/' in pfd:
        pfd = datetime.strptime(pfd, "%d/%m/%Y")
        nfd = pfd.strftime("%d %B %Y")
        nfd = str(nfd)
        return nfd
    else:
        return pfd


def Price(string1):
    string = string1.split(";")
    c1 = string[3]
    c1 = datetime.strptime(c1, '%d %B %Y')
    c1 = c1.strftime('%Y-%m-%d')
    c1 = c1.split("-")
    c1 = date(int(c1[0]), int(c1[1]), int(c1[2]))

    c2 = string[4]
    c2 = datetime.strptime(c2, '%d %B %Y')
    c2 = c2.strftime('%Y-%m-%d')
    c2 = c2.split("-")
    c2 = date(int(c2[0]), int(c2[1]), int(c2[2]))

    day = (c2 - c1).days

    price_per_day = int(string[5]) // int(day)

    return price_per_day


def Days():
    x = input(" How Many Days Do you want this car ... And Don't Worry , We Will Make you Happy :) ")
    x = int(x)
    return x


def Final_Price(p, d):
    final_price = p * d
    return final_price


def To_What(d1, x):
    d1 = str(d1).split("-")

    d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))

    date2 = d1 + timedelta(x)

    return date2


def CompleteInfo(cl, cm, year, sd, ed, rb):
    print("please complete you Information")
    cl = str(cl)
    cm = str(cm)
    year = str(year)
    sd = str(FormatDate(sd))
    ed = str(FormatDate(ed))
    rb = str(rb)
    name = str(input(" Your Name(the dual) : "))
    id = str(input(" Your ID (9 digit) : "))
    while len(id) != 9 or (not id.isdigit()):
        print(" not valid ")
        id = str(input(" Your ID (9 digit) : "))
    dob = input(" Your BirthDay(DD/MM/YYYY) : ")
    dob = str(FormatDate(dob))
    mobile = str(input(" Your Mobile number to connect to you (10 digit):"))
    while len(mobile) != 10 or (not id.isdigit()):
        print(" Not Valid mobile number  ")
        mobile = str(input(" Your Mobile number to connect to you (10 digit): "))

    new_rental_info = str(
        name + ";" + id + ";" + dob + ";" + mobile + ";" + cl + ";" + cm + ";" + year + ";" + sd + ";" + ed + ";" + rb)

    return new_rental_info


def Start():
    print("\n***** Welcome to the Car Gallery ******\n")
    d2, m2, y2 = [int(x) for x in input("Please Enter The Rental Dates   (DD/MM/YYYY) : ").split('/')]
    print(" * Just Wait A Little To Show The Car's Available ...\n  ")
    date1 = date(y2, m2, d2)

    file_name = "CarRentalCompleted.txt"

    count = LineOfFile(file_name)
    val = False
    chosen_car = [''] * count
    chosen_price = [''] * count
    i = 0
    ii = 0
    file = open("CarRentalCompleted.txt", "r+")
    for line in file:
        if line == "\n":
            break
        else:
            line = str(line)

            line = line.split(";")
            date_of_line = str(line[8])

            date_of_line = datetime.strptime(date_of_line, '%d %B %Y')
            date_of_line = date_of_line.strftime('%Y-%m-%d')
            date_of_line = date_of_line.split("-")
            date_of_line = date(int(date_of_line[0]), int(date_of_line[1]), int(date_of_line[2]))

            if date1 == date_of_line or date1 > date_of_line:
                val = True
                chosen_car[i] = line[4] + ";" + line[5] + ";" + line[6] + ";" + line[7] + ";" + line[8] + ";" + line[9]
                price_per_day = Price(chosen_car[i])
                i += 1

                print(" The car number " + str(i) + " is : " + line[5] + " | Model : " + line[
                    6] + "| The car license number is : " + line[4] + " | " + str(price_per_day) + " Per Day ")

    if val == False:
        print(" Sorry ... No Car Available Now !! ")

    else:
        f = int(input(" Press The Number That Represents The Car That you Want : "))
        days = Days()
        date2 = To_What(date1, days)
        price = Final_Price(price_per_day, days)
        chosen_car_info = chosen_car[f-1]
        chosen_car_info = chosen_car_info.split(";")

        new_rental_info = CompleteInfo(chosen_car_info[0], chosen_car_info[1], chosen_car_info[2], date1, date2, price)
        file.write(new_rental_info+"\n")

        print("\nThank You .. All Done\n")

    file.close()



