from Menu import Pizza, Burger, Drinks, Menu
from Resturant import Resturant
from Users import Chef , customer, Server, Manager
from Order import Order
def main():

    menu=Menu()

    pizza_1=Pizza('shhutki pizza ', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2=Pizza('Alur vorta pizza', 400, 'large',['potato','onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3=Pizza(' Dal pizza', 500, 'large', ['dal','oil'])
    menu.add_menu_item('pizza', pizza_3)

    #add burger to the menu
    burger_1=Burger('Naga_burger', 1000, 'chicken', ['bread', 'chilli'])
    menu.add_menu_item('burger', burger_1)
    burger_2=Burger('Beef burger', 1200,'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke=Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee=Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks',coffee)

    #show menu
    menu.show_menu()

    #add employes
    resturant=Resturant('Sai baba resturant',2000,menu)
    # manager=Manager('kala chan Manager', 5, 'kala@chan.com', 'kalipur',1500, 'jan 1 2020','core')
    # resturant.add_employee('manager',manager)

    chef=Chef('name', 1233, '@gmail.com','something', 3000, '1 2 2023', 'chef','noodels')
    #Chef=chef('rustom babouchi', 6, 'chap@com', 'rustonagar', 3500, 'Feb 1 2020', 'chef','noodoles')
    resturant.add_employee('chef', chef)

    server=Server('Chotu server', 8, 'naijai@com','resturant', 200, 'March 1 2020',' server')
    resturant.add_employee('server', server)


    #add employee
    resturant.show_employess()

    resturant=Resturant('adda resturant', 2000, menu)
    manager=Manager('kala', 56, '@.com','kaliapur', 1500, '01 january', 'core')
    resturant.add_employee('manager', manager)
    chef=Chef('babuchi', 202, '@gmail.com', 'wikitoki', 2000, '01 january', 'chef', 'everything')
    resturant.add_employee('chef', chef)

    #show_employess
    resturant.show_employee()


    #customer 1 placeing an order
    customer_1=customer('sakib', 5667,'@mail.com','jigatola',1000 )
    order_1=Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    resturant.add_order(order_1)

    #customer one paying for order order_1
    resturant.recive_payment(order_1, 2000, customer_1)
    print('revenue after firsr customer:',resturant.revenue, 'balance: ',resturant.balance)

    #customer 2 placeing an order
    customer_2=customer('sakib al hasan', 5667,'@mail.com','jigatola',1000 )
    order_2=Order(customer_1, [pizza_1, burger_2])
    customer_2.pay_for_order(order_2)
    resturant.add_order(order_2)

    #customer one paying for order order_1
    resturant.recive_payment(order_1, 5000, customer_1)
    print('revenue after second customer:',resturant.revenue, 'balance: ',resturant.balance)

    #pay rent
    resturant.pay_expanse(resturant.rent, 'Rent')
    print('After rent', resturant.revenue, resturant.balance, resturant.expense)

    resturant.pay_salary(chef)
    print('After salary', resturant.revenue, resturant.balance, resturant.expense)


#Call the main method
if __name__ == '__main__':
    main()