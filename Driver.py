import FixOldDatabase                      # import the module that is wanted For my Programming
import AddNewCarRental
import InquiryInfomation
import GetStatisticsInfo

while True:       # While the user doesn't choose the exit mode
    print("\n\n***** Welcome To The Car Rental Company *****\n\n"      # Welcome Message 
          " To Continue press [1] :\n"
          " To Exit press [2] ")
    x = input(" Press Here : ")
    while int(x) not in range(1, 3):                      # while loop to input the truth value
        print(" Not Valid Input .. Try Again  ")
        x = input(" Press Here : ")

    if int(x) == 1:                   # if the user press 1 Run the wanted Things

        print("\n\n\nPlease Select One Of The Following:\n\n"   # menu about the wanted things ( input by the user ) 
              " 1 - Fix Old Data Base\n"
              " 2 - Get Some Information\n"
              " 3 - Add New Car Renal\n"
              " 4 - Get Some Information about our cars here\n")
        choice = input(" Press Here : ")
        while int(choice) not in range(1, 5):
            print(" Not Valid Input .. Try Again ")
            choice = input(" Press Here : ")
        if int(choice) == 1:
            FixOldDatabase.Start()    # run the FixOldData module Start from Starts function
        elif int(choice) == 2:
            InquiryInfomation.Start()
        elif int(choice) == 3:
            AddNewCarRental.Start()
        elif int(choice) == 4:
            GetStatisticsInfo.Start()

    else:
        exit()
