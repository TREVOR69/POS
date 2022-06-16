import random


def customeroperations():
    print("[1]. Add customer")
    print("[2]. Delete customer")
    print("[3]. Update customer")
    print("[4]. Main Menu")

    selection = int(input("Choose One Option: "))

    while selection:
        if selection == 1:
            addcustomer()
            break
        elif selection == 2:
            deletecustomer()
            break
        elif selection == 3:
            updatecustomer()
            break
        elif selection == 4:
            from main import menu
            menu()
            break


def addcustomer():
    custid = random.randint(10000, 100000)
    custname = input("ENTER CUSTOMER NAME: ")
    custphone = input("ENTER CUSTOMER PHONE NUMBER: ")

    z = f'{custid},{custname},{custphone}\n'

    with open('customer.txt', 'a') as outfile:
        print("Customer Added successfully.")
        outfile.write(z)


def updatecustomer():
    with open("customer.txt", "r") as s:
        slist = s.readlines()
        cid = input("ENTER CUSTOMER ID: ")
        for Line in slist:
            if cid in Line:
                line_index = slist.index(Line)

                user_input = input("ENTER NEW PHONE NUMBER: ")
                k = Line.split(',')
                k[2] = user_input
        s = ','
        slist[line_index] = s.join(k)

        with open('customer.txt', 'w') as outfile:
            print("Customer Updated successfully.")
            for Line in slist:
                outfile.write(Line)


def deletecustomer():
    with open("customer.txt", "r") as s:
        slist = s.readlines()
        cid = input("ENTER CUSTOMER ID: ")
        for Line in slist:
            if cid in Line:
                line_index = slist.index(Line)

                slist.pop(line_index)

        with open('customer.txt', 'w') as outfile:
            print("Customer Deleted successfully.")
            for Line in slist:
                outfile.write(Line)
