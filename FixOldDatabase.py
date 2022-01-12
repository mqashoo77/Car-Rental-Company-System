from datetime import datetime

ddr = 0
dup = 0
pnc = 0
nmd = 0
nmr = 0
idd = 0
idr = 0
dobd = 0
dobr = 0
mobiled = 0
mobiler = 0
cld = 0
cmd = 0
cmr = 0
yeard = 0
yearr = 0


def ChangeFormatDate(date):
    str1 = date
    global ddr

    if '/' in str1:
        str1 = str1.replace('/', ' ')
        str1 = datetime.strptime(str1, "%d %m %Y")
        str1 = str1.strftime("%d %B %Y")
        ddr += 1
        return str1
    elif '-' in str1:
        str1 = str1.replace('-', ' ')
        str1 = datetime.strptime(str1, "%d %m %Y")
        str1 = str1.strftime("%d %B %Y")
        ddr += 1
        return str1
    else:
        return str1


def ModifyDate(line):
    a = str(line)
    a = a.split(";")
    a[2] = ChangeFormatDate(a[2])
    a[7] = ChangeFormatDate(a[7])
    a[8] = ChangeFormatDate(a[8])
    a = ';'.join(a)
    return a


def FindMessing(m_line, i, n , nof):
    b = m_line.split(";")
    x = i

    if x in range(0, 4):
        fo = open(nof, "r+")
        r = fo.readlines()
        for a in range(0, len(r)):
            if a == n:
                continue
            else:
                if r[a].split(";")[1] == b[1]:
                    b[i] = r[a].split(";")[i]
                elif r[a].split(";")[3] == b[3]:
                    b[i] = r[a].split(";")[i]

        fo.close()
    elif i == 5 or i == 6:
        fo = open(nof, "r+")
        r = fo.readlines()
        for a in range(0, len(r)):
            if a == n:
                continue
            else:
                if r[a].split(";")[4] == b[4]:
                    b[i] = r[a].split(";")[i]

    else:
        b[i] = b[i]

    return b[i]


def CheckMissingInfo(line, n , nof):
    a = line.split(";")
    global nmd, nmr, idd, idr, dobd, dobr, mobiled, mobiler, cld, cmd, cmr, yeard, yearr
    for i in range(len(a)):
        if a[i] == "":
            if i == 0:
                nmd += 1
            elif i == 1:
                idd += 1
            elif i == 2:
                dobd += 1
            elif i == 3:
                mobiled += 1
            elif i == 4:
                cld += 1
            elif i == 5:
                cmd += 1
            elif i == 6:
                yeard += 1
            a[i] = FindMessing(line, i, n , nof)
            if i == 0:
                if a[0] != "":
                    nmr += 1
            elif i == 1:
                if a[1] != "":
                    idr += 1
            elif i == 2:
                if a[2] != "":
                    dobr += 1
            elif i == 3:
                if a[3] != "":
                    mobiler += 1
            elif i == 5:
                if a[5] != "":
                    cmr += 1
            elif i == 6:
                if a[6] != "":
                    yearr += 1

    line = ";".join(a)

    return line


def RemoveDuplicate():
    global dup
    new_file = ""
    lines_seen = []  #  list to set the read line on it
    infile = open('CarRentalCompleted.txt', "r+")
    s = infile.readlines()
    for i in range(0, len(s)-1):
        if s[i] not in lines_seen:  # not a duplicate
            new_file += s[i]
            lines_seen.append(s[i])
    infile.truncate(0)                     # reset the file to add the new line with no Duplicate to it
    outfile = open('CarRentalCompleted.txt', "w")
    outfile.write(new_file)
    outfile.close()
    dup = len(s) - len(lines_seen)        # Get The Number of duplicate entries


def PrintSummary():
    print(" \n**** Summary of data missing in the database: \n")
    print("Number of duplicate entries in the database = " + str(dup))
    print("Number of entries with wrong date format in the database = " + str(ddr))
    print("Number of entries where names are dropped from the database = " + str(nmd))
    print("Number of entries where Ids are dropped from the database = " + str(idd))
    print("Number of entries where dob are dropped from the database = " + str(dobd))
    print("Number of entries where mobile are dropped from the database = " + str(mobiled))
    print("Number of entries where licence car  are dropped from the database = " + str(cld))
    print("Number of entries where car make  are dropped from the database = " + str(cmd))
    print("Number of entries where Model (year)  are dropped from the database = " + str(yeard))
    print("Number of entries where personal entry not be completed = " + str(pnc))

    print(" \n**** Summary of data recovered in the database:\n ")
    print("Number of duplicate entries removed from new database = " + str(dup))
    print("Number of entries with wrong date format fixed in the database = " + str(ddr))
    print("Number of entries where names are recovered from the database = " + str(nmr))
    print("Number of entries where Ids are recovered from the database = " + str(idr))
    print("Number of entries where dob are recovered from the database = " + str(dobr))
    print("Number of entries where mobile are recovered from the database = " + str(mobiler))
    print("Number of entries where car make are recovered from the database = " + str(cmr))
    print("Number of entries where Model (year) are recovered from the database = " + str(yearr))

    print("DONE")


def Start():
    print("\n ***** Welcome to Fix Old Data Center ***** \n")  # Welcom messege
    print(" * To Continue press [1] : \n"
          " TO Exit press [2] ")
    x = input(" Press Here : ")
    while int(x) not in range(1, 3):  # Get the feedback from user with limiting acces
        print(" Not Valid Input ")  # if the user doesnt press 1 to continue this messege will out
        print(" * To Continue press [1] :\n "
              " TO Exit press [2] ")
        x = input(" Press Here : ")
    if int(x) == 1:

        try:
            nof = input("Please Enter The Name of File you want to fixed it : ")

            global pnc
            file_name = str(nof)

            for c in range(0,3):
                if c == 0:
                    new_file_content = ""
                    fo = open(file_name, "r+")
                    for line in fo:
                        new_line = ModifyDate(line)
                        new = line.replace(line, new_line)
                        new_file_content += new
                    fo.truncate(0)
                    fo.close()
                    fo = open(file_name, "w")
                    fo.write(new_file_content)
                    fo.close()
                elif c == 1:
                    new_file_content1 = ""
                    new_file_content2 = ""
                    fo = open(file_name, "r+")
                    s = fo.readlines()
                    for i in range(0, len(s)):
                        new_line = CheckMissingInfo(s[i], i, nof)
                        a = new_line.split(";")
                        if a[0] == "" or a[1] == "" or a[1] == "" or a[2] == "" or a[3] == "" or a[4] == "" or a[
                            5] == "" or a[
                            6] == "" or a[7] == "" or a[8] == "" or a[9] == "":
                            new_file_content1 += new_line
                            writing_file = open("CarRentalMissing.txt", "w")
                            writing_file.write(new_file_content1)
                            writing_file.close()
                        else:
                            new_file_content2 += new_line
                            writing_file = open("CarRentalCompleted.txt", "w")
                            writing_file.write(new_file_content2)
                            writing_file.close()

                    fo.close()
                    file_messing = open("CarRentalMissing.txt", "r+")
                    fm = file_messing.readlines()
                    pnc = len(fm)
                    file_messing.close()
                else:
                    RemoveDuplicate()

            PrintSummary()

        except:

            print(" The Name of file not correct  ")
            print(" TO Try Again press 1\n"
                  " TO Return To The Main Menu press 2")
            z = input(" Press Here : ")
            while int(z) not in range(1, 3):
                print(" Not Valid Input ")
                z = input(" Press Here  [1/2] : ")
            if int(z) == 1:
                Start()
    else:
        exit()



