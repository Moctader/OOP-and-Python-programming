class user:
    def __init__(self, username, password):
        self.username=username
        self.password=password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_des=from_des
        self.to=to
        self.seat=["empty" for i in range(20)]


# b=Bus(2, "k", "12", "12.30", "Dhaka", "chi")
# print(vars(b))

class Phitron:
    totall_bus=5
    totall_bus_list=[]

    def add_bus(self):
        bus_no=int(input("Enter Bus No: "))
        flag=1
        for w in self.totall_bus_list:
            if bus_no==w['coach']:
                print("Bus Already Added")
                flag=0
                break

        if flag:
            bus_driver=input("Enter Bus Driver Name: ")
            bus_arrival=input("Enter Bus Arrival Time: ")  
            bus_departure=input("Enter Bus derparture Time: ")  
            bus_from=input("Enter Bus start from: ")
            bus_to=input("Enter bus destination: ")
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival, bus_departure,bus_from,bus_to)
            self.totall_bus_list.append(vars(self.new_bus)) #seat no didn't pass
            print("\n Add Bus Successfully")


# company=Phitron()
# company.add_bus()

class counter(Phitron):

    user_list=[]
    def reservation(self):
        bus_no=int(input("enter bus no: "))

        for w in self.totall_bus_list:
            if bus_no==w['coach']:
                passenger=input("Enter your Name: ")
                seat_no=int(input("Enter your seat_no: "))

                if seat_no>20:
                    print("Seat is not available")

                elif w['seat'][seat_no-1] !="empty":
                    print("Seat already reserved")
                else:
                    w['seat'][seat_no-1] =passenger

            else:
                print("No Bus Available")

#         for bus in self.totall_bus_list:
#             print(bus['seat'])      

# company=Phitron()
# company.add_bus()

# c=counter()
# c.reservation()
    def show_ticket(self):
        bus_no=int(input("Enter bus no: "))

        for w in self.totall_bus_list:
            if bus_no==w['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Arrival: {w['arrival']} \t\t\t Departure Time: {w['departure']} \n From: {w['from_des']} \t\t\t To: {w['to']} ")
                print()
                

                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a+=1
                    
                    

                    for j in range (2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a+=1
                    print('\n')
                print('*'*50)




# company=Phitron()
# company.add_bus()

# c=counter()
# c.show_ticket()

    def create_account(self):
        name=input("Enter your username: ") #
        password=input("Enter your password: ")
        self.new_user=user(name, password)
        self.user_list.append(vars(self.new_user))


    def available_buses(self):
        if len(self.totall_bus_list)==0:
            print("No Buses available")
        else:
            print('*'*50)
            for bus in self.totall_bus_list:
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}{' '*10}))")
                print(F"BUS NUMBER: {bus['coach']} \t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t\t Departure Time: {bus['departure']} \n From: {bus['from_des']} \t\t\t To: {bus['to']} ")
            print('*'*50)

    def get_users(self):
        return self.user_list
    
# company=Phitron()
# company.add_bus()

# c=counter()
# c.available_buses()

while True:

    company=Phitron()
    b=counter()
    print("1. Create an account\n2. login to your account\n3. exit")
    user_input=int(input("Enter your choice:"))
    if user_input==3:
        break
    elif user_input==1:
        b.create_account()
    elif user_input==2:
        name=input("Enter your Username: ")
        password=input("Enter your password: ")

        flag=0
        isAdmin=False
        if name=="admin" and password=="123":
            isAdmin=True
        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and user['password']==password: #
                    flag=1
                    break

            if flag:
                while True:
                    print("Welcome to Bus Ticket Booking System")
                    print("1. Available Buseu\n2. Show Bus info\n3. Reservation\n4. Exit")
                    a=int(input("Enter your choice"))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
            else:
                print("No user found")

        
        else:
            while True:
                print("Hello admin")
                print("1. Add Bus\n2. Available Buses\n3. Show bus info\n4. Exit")
                a=int(input("Enter your choice"))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show_ticket()


