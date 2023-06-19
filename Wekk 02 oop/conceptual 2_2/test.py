class user:
    def __init__(self, username, password) -> None:
        self.username=username
        self.password=password

class Bus:
    def __init__(self, coach,driver, arrival, destination, from_des, to) -> None:
        self.driver=driver
        self.coach=coach
        self.arrival=arrival
        self.destination=destination
        self.from_des=from_des
        self.to=to
        self.seat=["empty" for i in range(20)]


class phitron:
    totall_bus=5
    totall_bus_list=[]

    def add_bus(self):
        bus_no=int(input("Enter the no: "))
        flag=1
        for w in self.totall_bus_list:
            if bus_no==w['coach']:
                print('Bus already added')
                flag=0
                break
            if flag:
                driver_name=input("driver name: ")
                coach_name=input("coach name: ")
                arrival_time=input("arrival time: ")
                destination_time=input("destination time: ")
                from_des=input("from_des: ")
                to=input("t0: ")
                self.new_bus=Bus(driver_name,coach_name,arrival_time,destination_time,from_des,to)
                self.totall_bus_list.append(vars(self.new_bus))
                print()

company=Bus('r','k',7,8,'c','t')
print(vars(company))

val=phitron()
val.add_bus()