x = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = 10 #int(input('Enter number of Row - \n'))
Seats =15 # int(input('Enter number of seats in a Row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]
users =["user1"]
passwords = ["pass1"]
ausers =["shreyes"]
apasswords = ["pa$$word"]


def login(username,password):
    if username in users and passwords[users.index(username)]==password:
        return "user"
    elif username in ausers and apasswords[ausers.index(username)]==password:
        return "admin"
    else:
        flag=input("would you link to signup(y/n)")
        if flag=="y":
            signup(username,password)
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

def display_chart(Seats,table_of_chart):
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
    print('Vacant Seats = ', Total_seat - Booked_seat)
    print()

def buy_ticket(table_of_chart,Booked_seat,Total_Income):
    Row_number = int(input('Enter Row Number - \n'))
    Column_number = int(input('Enter Column Number - \n'))
    if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
        if table_of_chart[str(Row_number-1)][str(Column_number)] == 'O':
            if Row*Seats <= 60:
                prize_of_ticket = 180
            elif Row_number <= int(Row/2):
                prize_of_ticket = 200
            else:
                prize_of_ticket = 220
            print('prize_of_ticket - ', 'Rs.', prize_of_ticket)
            conform = input('y for booking and n for Stop booking - ')
            person_detail = {}
            if conform == 'y':
                person_detail['Name'] = input('Enter Name - ')
                person_detail['Gender'] = input('Enter Gender - ')
                person_detail['Age'] = input('Enter Age - ')
                person_detail['Phone_No'] = input('Enter Phone number - ')
                person_detail['Ticket_prize'] = prize_of_ticket
                table_of_chart[str(Row_number-1)][str(Column_number)] = 'X'
                Booked_seat += 1
                Total_Income += prize_of_ticket
            # else:
            #     continue
            Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
            print('Booked Successfully')
        else:
            print('This seat already booked by some one')
    else:
        print()
        print('***  Invalid Input  ***')
    print()

def display_seat_details():
    Enter_row = int(input('Enter Row number - \n'))
    Enter_column = int(input('Enter Column number - \n'))
    if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
        if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'X':
            person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
            print('Name - ', person['Name'])
            print('Gender - ', person['Gender'])
            print('Age - ', person['Age'])
            print('Phone number - ', person['Phone_No'])
            print('Ticket Prize - ', '$', person['Ticket_prize'])
        else:
            print()
            print('---**---  Vacant seat  ---**---')
    else:
        print()
        print('***  Invalid Input  ***')
    print()

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
        percentage = (Booked_seat/Total_seat)*100
        return percentage

class_call = chart
table_of_chart = class_call.chart_maker()
print("**LOGIN PAGE**")
loginuser = input("Enter Username: ")
loginpass = input("Enter Password: ")
if login(loginuser,loginpass)=="admin":
    while x != 0:
        print('1: Show the seats \n2: Buy a Ticket \n3: Statistics ',
            '\n4: for Show booked Tickets User Info \n0: for Exit')
        x = int(input('Select Option - '))

        
        if x == 1:
            display_chart(Seats,table_of_chart)
        
        elif x == 2:
            buy_ticket(table_of_chart,Booked_seat,Total_Income)
            
        elif x == 3:
            print('Number of purchased Ticket - ', Booked_seat)
            print('Percentage - ', class_call.find_percentage())
            print('Current  Income - ', 'Rs', prize_of_ticket)
            print('Total Income - ', 'Rs', Total_Income)
            print()

        elif x == 4:
            display_seat_details()

        elif x == 0:
            print("Visit again! Bye")

        else:
            print()
            print('***  Invalid Input  ***')
            print()
elif login(loginuser,loginpass)=="user":
     while x != 0:
        print('1: Show the seats \n2: Buy a Ticket \n0: Exit')
        x = int(input('Select Option - '))

        
        if x == 1:
            display_chart(Seats,table_of_chart)
        
        elif x == 2:
            buy_ticket(table_of_chart,Booked_seat,Total_Income)
        elif x == 0:
            print("Visit again! Bye")
        else:
            print()
            print('***  Invalid Input  ***')
            print()
else:
    print()
    print('***  Invalid Input  ***')
    print()
