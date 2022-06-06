import random
import os
import numpy as np


def productoperations():
    print("[1]. Add Product")
    print("[2]. Delete product")
    print("[3]. Update product")
    print("[0]. Main Menu")


def addproduct():
    list_to_write = []
    proid = random.randint(100, 10000)
    list_to_write.append(proid)
    proname = input("ENTER PRODUCT NAME: ")
    list_to_write.append(proname)
    protype = input("ENTER PRODUCT TYPE: ")
    list_to_write.append(protype)
    proquantity = int(input("ENTER PRODUCT QUANTITY: "))
    list_to_write.append(proquantity)
    price = int(input("ENTER PRICE OF PRODUCT: "))
    list_to_write.append(price)
    s = str(list_to_write)
    y = s.strip('[]')
    z = y.split(',')

    with open('products.txt', 'a') as outfile:
        outfile.write("\n")
        outfile.write(str(z))


def updateproduct():
    lt = []
    elt = []
    with open("products.txt", "r") as s:
        cid = int(input("ENTER PRODUCT ID: "))
        for Line in s:
            if str(cid) in Line:
                line1 = Line.strip("[]")
                line11 = line1.strip("()")
                line2 = line11.split(',')
                lt.append(line2)
                user_input = input("ENTER NEW QUANTITY: ")
                lt[0].pop(3)
                lt[0].insert(3, user_input)
                lt1 = str(lt)
                lt2 = lt1.strip('[ ')
                lt3 = lt2.rstrip(']')
                lt4 = eval(lt3)
                print(lt4)
                #lt4 = str(lt4)
                #lt5 = lt4.strip('()')
                #lt6 = lt5.split(',')
                #elt.append(lt6)
                #with open('products.txt', 'a') as t:
                    #t.write("\n")
                    #t.write(str(elt))
            #elif str(cid) != Line:
                #with open('products.txt', 'r') as w:
                    #for Line1 in w:
                        #if str(cid) != Line1:
                            #k = Line1
                #with open('products.txt', 'a') as q:
                    # q.write("\n")
                    #q.write(k)


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
