import random


def productoperations():
    print("[1]. Add Product")
    print("[2]. Delete product")
    print("[3]. Update product")
    print("[4]. Main Menu")

    selection = int(input("choose one option: "))

    while selection:
        if selection == 1:
            addproduct()
            break
        elif selection == 2:
            deleteproduct()
            break
        elif selection == 3:
            updateproduct()
            break
        elif selection == 4:
            from main import menu
            menu()
            break


def addproduct():
    proid = random.randint(100, 10000)
    proname = input("ENTER PRODUCT NAME: ")
    protype = input("ENTER PRODUCT TYPE: ")
    proquantity = int(input("ENTER QUANTITY IN NUMBERS: "))
    price = int(input("ENTER PRICE OF PRODUCT: "))
    z = f'{proid},{proname},{protype},{proquantity},{price}\n'

    with open('products.txt', 'a') as outfile:
        print('Product succefully added')
        outfile.write(z)


def updateproduct():
    with open("products.txt", "r+") as s:
        slist = s.readlines()
        cid = input("ENTER PRODUCT ID: ")
        for Line in slist:
            if cid in Line:
                line_index = slist.index(Line)
                user_input = input("Enter New Quantity: ")
                new_price = input("Enter New Price: ")
                k = Line.split(',')
                k[3] = user_input
                k[4] = new_price
        s = ','
        slist[line_index] = s.join(k)

        with open('products.txt', 'w') as outfile:
            print('Product succefully Updated')
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
            print('Product succefully deleted')
            for Line in slist:
                outfile.write(Line)

