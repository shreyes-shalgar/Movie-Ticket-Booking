import os

Row = 10 #int(input('Enter number of Row - \n'))
Seats = 6 # int(input('Enter number of seats in a Row - \n'))
Total_Income = 0
prize_of_ticket = 0
Total_seat = Row*Seats
movie_db ={"mid":[1,2,3],"mname":["Avatar 2","Inception", "Avengers"], "tid":[1,1,1], "show_timing": ["10am","12pm","9am"]}
theatre_db ={"tid":[1],"tname":["ESquare"],"city":["Solapur"]}
tmid=-10     #arbitrary
x = 10      #arbitrary
Booked_ticket_Person = [[[None for j in range(Seats)] for i in range(Row)]for k in range(len(movie_db['mid']))]
Booked_seat = [0 for i in range(len(movie_db['mid']))]

users =["user1"]
passwords = ["pass1"]
ausers =["shreyes","1"]
apasswords = ["pa$$word","1"]
def login(username,password):
    if username in users and passwords[users.index(username)]==password:
        print("Logged in\n")
        return "user"
    elif username in ausers and apasswords[ausers.index(username)]==password:
        print("Logged in as admin\n")
        return "admin"
    else:
        flag=input("Would you like to Sign-up (y/n)")
        if flag=="y":
            signup(username, password)
            # print("Logged in\n")
            return "user"
        else:
            return "na"

def signup(username,password):
    if username in users:
        print ("please select different username")
    else:
        users.append(username)
        passwords.append(password)
        print("Signed up successfully\n")

def display_chart(table_of_chart):
    print()
    if Seats < 10:
        for seat in range(Seats):
            print(seat, end='  ')
        print(Seats)
    else:
        for seat in range(10):
            print(seat, end='  ')
        for seat in range(10, Seats):
            print(seat, end=' ')
        print(Seats)
    if Seats < 10:
        for num in table_of_chart.keys():
            print(int(num)+1, end='  ')
            for no in table_of_chart[num].values():
                print(no, end='  ')
            print()
    else:
        count_num = 0
        for num in table_of_chart.keys():
            if int(list(table_of_chart.keys())[count_num]) < 9:
                print(int(num)+1, end='  ')
            else:
                print(int(num)+1, end=' ')
            count_key = 0
            for no in table_of_chart[num].values():
                if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                    print(no, end='  ')
                else:
                    print(no, end='  ')
                count_key += 1
            count_num += 1
            print()
    print('Vacant Seats = ', Total_seat - Booked_seat[tmid])
    print()

def buy_ticket(table_of_chart,arr):
    Row_number = int(input('Enter Row Number - '))
    Column_number = int(input('Enter Column Number - '))
    if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
        if table_of_chart[str(Row_number-1)][str(Column_number)] == 'O':
            if Row*Seats <= 60:
                prize_of_ticket = 180
            elif Row_number <= int(Row/2):
                prize_of_ticket = 200
            else:
                prize_of_ticket = 220
            print('Prize of Ticket - ', 'Rs.', prize_of_ticket)
            conform = input('\nConfirm booking (y/n) - ')
            person_detail = {}
            if conform == 'y':
                print("\n**Enter Personal details**\n")
                person_detail['Name'] = input('Enter Name - ')
                person_detail['Gender'] = input('Enter Gender - ')
                person_detail['Age'] = input('Enter Age - ')
                person_detail['Phone_No'] = input('Enter Phone number - ')
                person_detail['Ticket_prize'] = prize_of_ticket
                table_of_chart[str(Row_number-1)][str(Column_number)] = 'X'
                arr[0] += 1
                arr[1] += prize_of_ticket
                print('\nBooked Successfully\n')
                Booked_ticket_Person[tmid][Row_number-1][Column_number-1] = person_detail
                
                return arr
            else:
                print('Skipped booking')
                  
        else:
            print('This seat already booked by someone')
    else:
        print('\n***  Invalid Input  ***\n')

def display_seat_details(mdb,toc):
    display_movie(mdb)
    Enter_mid = int(input('\nEnter Movie id - '))-1
    display_chart(toc)
    Enter_row = int(input('Enter Row number - '))
    Enter_column = int(input('Enter Column number - '))
    if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
        if table_of_chart[Enter_mid-1][str(Enter_row-1)][str(Enter_column)] == 'X':
            person = Booked_ticket_Person[Enter_mid][Enter_row - 1][Enter_column - 1]
            print('Name - ', person['Name'])
            print('Gender - ', person['Gender'])
            print('Age - ', person['Age'])
            print('Phone number - ', person['Phone_No'])
            print('Ticket Prize - ', '$', person['Ticket_prize'])
            print()

        else:
            print('\n---**---  Vacant seat  ---**---\n')
    else:
        print('\n***  Invalid Input  ***\n')

def add_movie(mdb):
    print("**Enter New Movie Details**\n")
    mid = mdb['mid'][-1]+1
    mname = input("Movie Name: ")
    tid = input("Theatre id: ")
    show_timing = input("Show Timing: ")
    mdb["mid"].append(mid)
    mdb["mname"].append(mname)
    mdb["tid"].append(tid)
    mdb["show_timing"].append(show_timing)
    table_of_chart.append(class_call.chart_maker())
    Booked_seat.append(0)
    display_movie(mdb)

def add_threatre(tdb):
    print("**Enter New Theatre Details**\n")
    tid = tdb['tid'][-1]+1
    tname = input("Theatre Name: ")
    city = input("City: ")
    tdb["tid"].append(tid)
    tdb["tname"].append(tname)
    tdb["city"].append(city)
    display_theatre(tdb)
    # table_of_chart.append(class_call.chart_maker())
    # Booked_seat.append(0)

def display_movie(mdb):
    print("  ***Movie Table***  ")
    print("Movie id","\t","Movie","\t\t","Theatre id","\t","Show Timing")
    for i in range(len(mdb['mid'])):
        print(mdb["mid"][i],"\t\t", mdb["mname"][i],"\t", mdb["tid"][i],"\t\t", mdb["show_timing"][i])

def display_theatre(tdb):
    print("  ***Theatre Table***  ")
    print("Theatre Id","\t","Theatre","\t","City")
    for i in range(len(tdb['tid'])):
        print(tdb["tid"][i],"\t\t", tdb["tname"][i],"\t", tdb["city"][i])

class chart:
    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'O'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (sum(Booked_seat)/Total_seat)*100
        return round(percentage,2)

class_call = chart
table_of_chart = [class_call.chart_maker() for i in range(len(movie_db["mid"]))]


os.system('cls||clear')
print("----MOVIE TICKET BOOKING SYSTEM----\n")
print("       ****LOGIN PAGE****     \n")
loginuser = input("Enter Username: ")
loginpass = input("Enter Password: ")
if login(loginuser,loginpass)=="admin":
    while x != 0:
        click=input("\n -----Press Enter to continue----- \n")
        os.system('cls||clear')
        flag=0
        print("\n----MOVIE TICKET BOOKING SYSTEM----\n")
        print('1: View Available seats \n2: Buy a Ticket \n3: Statistics ',
            '\n4: Show booked Tickets User Info.\n5: Add New Movie\n6: Add New Theatre \n0: Exit')
        x = int(input('Select Option - '))
        print()
        if x == 1:
            display_movie(movie_db)
            tmid = int(input("\nSelect Movie Id: "))-1
            display_chart(table_of_chart[tmid])
            flag+=1
        
        elif x == 2:
            if flag<1:
                display_movie(movie_db)
                tmid = int(input("\nSelect Movie Id: "))-1
                display_chart(table_of_chart[tmid])
            Booked_seat[tmid],Total_Income = buy_ticket(table_of_chart[tmid],[Booked_seat[tmid],Total_Income])
            # print(Booked_seat[tmid])
            
        elif x == 3:
            if flag<1:
                display_movie(movie_db)
                tmid = int(input("\nSelect Movie Id: "))-1
            print('Number of purchased Ticket for selected movie- ', Booked_seat[tmid])
            print('Total Number of purchased Ticket - ', sum(Booked_seat))
            print('Percentage - ', class_call.find_percentage(),"%")
            # print('Current  Income - ', 'Rs', prize_of_ticket)
            print('Total Income - ', 'Rs', Total_Income)
            print()

        elif x == 4:
            display_seat_details(movie_db,table_of_chart[tmid])
        
        elif x == 5:
            add_movie(movie_db)

        elif x == 6:
            add_threatre(theatre_db)
        
        elif x == 0:
            print("Visit again! Bye")

        else:
            print('\n***  Invalid Input  ***\n')

elif login(loginuser,loginpass)=="user":
     while x != 0:
        click=input("---**---  Press Enter to continue---**---  \n")
        os.system('cls||clear')
        flag=0
        print("\n----MOVIE TICKET BOOKING SYSTEM----\n")
        print('1: View Available seats \n2: Buy a Ticket \n0: Exit')
        x = int(input('Select Option - '))
        print()
        if x == 1:
            display_movie(movie_db)
            tmid = int(input("\nSelect Movie Id: "))-1
            display_chart(table_of_chart[tmid])
            flag+=1
        
        elif x == 2:
            if flag<1:
                display_movie(movie_db)
                tmid = int(input("\nSelect Movie Id: "))-1
                display_chart(table_of_chart[tmid])
            Booked_seat[tmid],Total_Income = buy_ticket(table_of_chart[tmid],[Booked_seat[tmid],Total_Income])
        elif x == 0:
            print("Visit again! Bye")
        else:

            print('\n***  Invalid Input  ***\n')

else:
    print('\n***  Invalid Input  ***\n')
