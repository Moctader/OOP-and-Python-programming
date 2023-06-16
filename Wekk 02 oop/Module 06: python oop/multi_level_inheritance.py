class vehicle:
    def __init__ (self, color, price):
        self.color=color
        self.price=price

class bus(vehicle):
    def __init__(self, color, price, seat):
        self.seat=seat
        super().__init__(color, price)

class truck(bus):
    def __init__(self, color, price, seat, weight):
        self.weight=weight
        super().__init__(color, price, seat)

class acbbus(bus):
    def __init__(self, color, price, seat, temperature):
        self.tenperature=temperature
        super().__init__(color, price, seat)