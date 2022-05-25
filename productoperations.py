import random
import os


def productoperations():
    print("[1]. Add Product")
    print("[2]. Delete product")
    print("[3]. Update product")
    print("[0]. Main Menu")


def addproduct():
    outfile = open('products.txt', 'a')
    prodid = random.randint(100, 10000)
    prodname = input("ENTER PRODUCT NAME: ")
    prodtype = input("ENTER PRODUCT TYPE: ")
    outfile.write(str(prodid) + " " + prodname + " " + prodtype + '\n')
    outfile.close()


def updateproduct():
    s = open("products.txt", "r")
    z = open("temp.txt", "w")

    cid = int(input("ENTER PRODUCT ID: "))
    f = ' '
    while f:
        f = s.readline()
        l = f.split(" ")
        if len(f) > 0:
            if int(l[0]) == cid:
                prodid = random.randint(100, 10000)
                prodname = input("ENTER PRODUCT NAME: ")
                prodtype = input("ENTER PRODUCT TYPE: ")

                z.write(str(prodid) + " " + prodname + " " + prodtype)

            else:
                z.write(f)

        s.close()
        z.close()

        os.remove("products.txt")
        os.rename("temp.txt", "products.txt")


def deleteproduct():
    s = open("products.txt", "r")
    z = open("temp.txt", "w")

    cid = int(input("ENTER PRODUCT ID"))
    f = ' '
    while f:
        f = s.readline()
        l = f.split(" ")
        if len(f) > 0:
            if int(l[0]) != cid:
                z.write(f)

        s.close()
        z.close()

        os.remove("products.txt")
        os.rename("temp.txt", "products.txt")


productoperations()
selection = int(input("Choose One Option: "))

while selection != 0:
    if selection == 1:
        addproduct()
    elif selection == 2:
        deleteproduct()
    elif selection == 3:
        updateproduct()

    productoperations()
    selection = int(input("choose one option: "))

print("Goodbye")
