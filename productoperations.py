import random


def addproduct():
    proid = random.randint(100, 10000)
    proname = input("ENTER PRODUCT NAME: ")
    protype = input("ENTER PRODUCT TYPE: ")
    proquantity = int(input("ENTER PRODUCT QUANTITY: "))
    price = int(input("ENTER PRICE OF PRODUCT: "))

    z = f'{proid},{proname},{protype},{proquantity},{price}\n'

    with open('products.txt', 'a') as outfile:
        outfile.write(z)


def updateproduct():
    with open("products.txt", "r") as s:
        slist = s.readlines()
        cid = input("ENTER PRODUCT ID: ")
        for Line in slist:
            if cid in Line:
                line_index = slist.index(Line)
                user_input = input("ENTER NEW QUANTITY: ")
                new_price = input("ENTER NEW PRICE: ")
                k = Line.split(',')
                k[3] = user_input
                k[4] = new_price
        s = ','
        slist[line_index] = s.join(k)

        with open('products.txt', 'w') as outfile:
            for Line in slist:
                outfile.write(Line)


def deleteproduct():
    with open("products.txt", "r") as s:
        slist = s.readlines()
        cid = input("ENTER PRODUCT ID: ")
        for Line in slist:
            if cid in Line:
                line_index = slist.index(Line)

                slist.pop(line_index)

        with open('products.txt', 'w') as outfile:
            for Line in slist:
                outfile.write(Line)


loop = 1

while loop == 1:

    def productoperations():
        print("[1]. Add Product")
        print("[2]. Delete product")
        print("[3]. Update product")
        print("[4]. Main Menu")

        productoperations()

        selection = int(input("Choose One Option: "))
        if selection == 1:
            addproduct()
        elif selection == 2:
            deleteproduct()
        elif selection == 3:
            updateproduct()
        elif selection == 4:
            updateproduct()
        else:
            print('WRONG SELECTION! Please Try Again! ')
