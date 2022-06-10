import json
import random


def searchproduct():
    lt = []
    with open("products.txt", "r") as z:
        pid = int(input("Enter Product Id: "))
        for Line in z:
            if str(pid) in Line:
                lt.append(Line)
                print(lt)


def checkcustomer():
    cid = input("Enter Customer Id: ")
    with open("customer.txt", "r") as v:
        custlist = v.readlines()
        for Line in custlist:
            if cid in Line:
                checkproduct()
                break
    return cid


def checkproduct():
    pid1 = input("Enter Product Id: ")

    with open("products.txt", "r") as p:
        productlist = p.readlines()
        for Line1 in productlist:
            if pid1 in Line1:
                print('product available')
                #checkproductquantity()
                break
            else:
                print('Not available')
                break
        return pid1


def checkproductquantity():
    pid2 = checkproduct()
    print(pid2)
    quantity = int(input("Quantity: "))
    with open("products.txt", "r") as v:
        prodlist = v.readlines()
        for Line in prodlist:
            if pid2 in Line:
                prod = Line.split(',')
                if prod[3] >= str(quantity):
                    makepurchase()
                    break
                else:
                    print("Quantity required is higher than the stock! Cannot make this sell!")
                    break
            else:
                print('Product does not exist!')
                break
    return quantity


def makepurchase():
    transaction_list = []
    purchase_dict = {}
    shopping_cart = []
    list_quantity = []
    list_price = []
    prod = []
    cid = checkcustomer()
    pid = checkproduct()
    quantity = checkproductquantity()
    loop1 = 1

    while loop1 == 1:
        add_item = input('Add product? Y/N?: ').upper()
        if add_item == 'Y':
            list_quantity.append(quantity)  # adding quantity to the declared empty list
            purchaseid = random.randint(2000, 2000000)
            with open("products.txt", "r") as s:
                sprodlist = s.readlines()
                for Line in sprodlist:
                    if pid in Line:
                        line_index = sprodlist.index(Line)
                        prod = Line.split(',')
                        pname = prod[1]
                        pquantity = prod[3]
                        pprice = prod[4]

            with open("customer.txt", "r") as t:
                for Line in t:
                    if str(cid) in Line:
                        cust = Line.split(',')
                        cname = cust[1]

            shopping_cart.append(pname)  # adding product name to the declared empty list
            newquantity = (int(pquantity) - quantity)
            totalprice = (int(pprice) * quantity)
            list_price.append(totalprice)  # adding the total price of product times quantity to the declared empty list
            prod[3] = str(newquantity)
            s = ','
            sprodlist[line_index] = s.join(prod)

            total = 0
            for i in range(0, len(list_price)):
                total = total + list_price[i]
            purchase_dict['Purchase ID'] = purchaseid
            purchase_dict['Customer Name'] = cname
            purchase_dict['Products Name'] = shopping_cart
            purchase_dict['Products Quantity'] = list_quantity
            purchase_dict['Cumulative Product Prices'] = list_price
            purchase_dict['Total'] = total

            with open('products.txt', 'w') as outfile:
                for Line in sprodlist:
                    outfile.write(Line)

        elif add_item == 'N':

            transaction_list.append(purchase_dict)
            with open('transactions.txt', 'a') as outfile1:
                outfile1.write('\n')
                outfile1.write(str(transaction_list))
            print("Purchase Successful!...")
            break

        else:
            print("WRONG SELECTION!...")


loop = 1

while loop == 1:

    def purchasemenu():
        print("[1]. Search Product")
        print("[2]. Sell")
        print("[3]. Main Menu")
        print("[4]. Exit")


    purchasemenu()
    selection = int(input("choose one option: "))
    if selection == 1:
        searchproduct()
    elif selection == 2:
        checkcustomer()
    elif selection == 3:
        makepurchase()  # edit this line
    elif selection == 4:
        loop = 0
        print('System Exit! Goodbye...')
    else:
        print("WRONG SELECTION!")
