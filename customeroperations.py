import random


def customeroperations():
    print("[1]. Add customer")
    print("[2]. Delete customer")
    print("[3]. Update customer")
    print("[0]. Main Menu")


def addcustomer():
    custid = random.randint(10000, 100000)
    custname = input("ENTER CUSTOMER NAME: ")
    custphone = input("ENTER CUSTOMER PHONE NUMBER: ")

    z = f'{custid},{custname},{custphone}\n'

    with open('customer.txt', 'a') as outfile:
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
            for Line in slist:
                outfile.write(Line)


customeroperations()
selection = int(input("Choose One Option: "))

while selection != 0:
    if selection == 1:
        addcustomer()
    elif selection == 2:
        deletecustomer()
    elif selection == 3:
        updatecustomer()
    else:
        print('WRONG SELECTION! ENTER EITHER 1 OR 2!')
        break
    customeroperations()
    selection = int(input("choose one option: "))

print("Goodbye")
