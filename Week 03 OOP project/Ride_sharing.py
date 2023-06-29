from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]

    def add_driver(self,driver):
        self.drivers.append(driver)
    
    def add_rider(self, rider):
        self.riders.append(rider)


    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers{len(self.add_drivers)}'   

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name=name
        self.email=email
        # Set user id dynamically
        self.__id=0
        self.__nid=nid
        self.wallet=0
       

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location
        super().__init__(name, email, nid)
        

    def display_profile(self):
        return f"name: {self.name} and email: {self.email}"
    
    def update_location(self, current_location):
        self.current_location=current_location
    
    def request_ride(self, destination):
        if not self.current_ride:
            #TODO: set ride properly
            # TODO: set current ride via ride match
            ride_request=Ride_Request(self, destination)
            ride_matcher=Ride_Matching()
            self.current_ride=ride_matcher.find_driver(ride_request)

class Driver(User):
    def __init__(self, name, email, nid, cuurent_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=cuurent_location
        self.wallet=0

        def display_profile(self):
            print (f'name: {self.name} email: {self.email}')

        def accept_ride(self, ride):
            ride.get_ride(self)


class Ride:
    def __init__(self, start_location, end_loation) -> None:
        self.start_location=start_location
        self.end_location=end_loation
        self.start_time=None
        self.end_time=None
        self.rider=None 
        self.esteemed_fare=None

    def set_driver(self, driver):
        self.driver=driver
    
    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self, amount):
        self.end_time=datetime.now()
        self.rider.wallet-=self.esteemed_fare
        self.driver.wallet+=self.esteemed_fare


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider=rider
        self.end_location=end_location

class Ride_Matching:
    def __init__(self) -> None:
        self.available_drivers=[]

    def find_driver(self):
        if len(self.available_drivers)>0:
            # TODO: Find the closest driver
            driver=self.available_drivers[0]
            ride=Ride(Ride_Request.rider.current_location, Ride_Request.end_location)
            driver.accept_ride(ride)
            return ride
                

class vehicle(ABC):

    speed={
        'car':50,
        'bike':60,
        'cng':15
    }
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        self.status='available'
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass


class car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status='unavailable'


#Check the class integration
neya_jao=Ride_sharing('niye jao')
sakib=Rider("sakib khan", "sakib@khan.com", 1254, 'Mohakhali',1200)
neya_jao.add_driver(sakib)
kala_pakhi=Driver('kala pakhi', 'kala@sada.com',5648, 'gulsan')
neya_jao.add_driver(kala_pakhi)
print(neya_jao)
