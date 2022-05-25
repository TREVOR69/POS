import os
import random


def customeroperations():
    print("[1]. Add customer")
    print("[2]. Delete customer")
    print("[3]. Update customer")
    print("[0]. Main Menu")


def addcustomer():
    outfile = open('customer.txt', 'a')
    custid = random.randint(10000, 100000)
    custname = input("ENTER CUSTOMER NAME: ")
    custphone = int(input("ENTER CUSTOMER PHONE NUMBER: "))
    outfile.write(str(custid) + " " + custname + " " + str(custphone) + '\n')
    outfile.close()


customeroperations()
selection = int(input("Choose One Option: "))

while selection != 0:
    if selection == 1:
        addcustomer()
    elif selection == 2:
        # productoperation()
        print("option 2 selected. ")

    elif selection == 3:
        s = open("customer.txt", "r")
        z = open("temp.txt", "w")

        cid = int(input("ENTER CUSTOMER ID"))
        f = ' '
        while f:
            f = s.readline()
            l = f.split(" ")
            if len(f) > 0:
                if int(l[0]) == cid:
                    custid = random.randint(10000, 100000)
                    custname = input("ENTER CUSTOMER NAME: ")
                    custphone = int(input("ENTER CUSTOMER PHONE NUMBER: "))

                    z.write(str(custid) + " " + custname + " " + str(custphone))

                else:
                    z.write(f)

            s.close()
            z.close()

            os.remove("customer.txt")
            os.rename("temp.txt", "customer.txt")
    customeroperations()
    selection = int(input("choose one option: "))

print("Goodbye")
