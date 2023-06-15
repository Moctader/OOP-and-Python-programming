class phone:
    Manufacture='china'

    def __init__(self, origin, name, cost):
        self.origin=origin
        self.name=name
        self.cost=cost

    def send_sms(self, phone, sms):
        text=f'send sms: {phone} {sms}'
        print(text)

my_phone=phone(' dhaka', 'smasung', 19000)
print(my_phone.origin, my_phone.name, my_phone.cost)

her_phone=phone('naogaon', 'iphone', 13000)
print(her_phone.origin, her_phone.name, her_phone.cost, her_phone.Manufacture)

message=phone('naogaon', 'iphone', 13000)
value=message.send_sms(400, 'value')