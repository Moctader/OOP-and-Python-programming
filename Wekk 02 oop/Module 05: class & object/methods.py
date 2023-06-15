class phone:
    price=19000
    name='samsung'
    features=['camera', 'speaker', 'hammer']

    def call(self):
        print('calling someone')

    def send_sms(self,phone, sms):
        text=f'the number is {phone}, the sms is {sms}'
        return text
    

my_phone=phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(444, 'dont call me')
print(result)