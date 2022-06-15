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


def makepurchase():
    transaction_list = []
    purchase_dict = {}
    shopping_cart = []
    list_quantity = []
    list_price = []
    prod = []
    cid = input("Enter Customer Id: ")

    loop1 = 1

    while loop1 == 1:
        add_item = input('Add product? Y/N?: ').upper()
        if add_item == 'Y':
            pid = input("Enter Product Id: ")
            quantity = int(input("Quantity: "))
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
                clist = t.readlines()
                for Line1 in clist:
                    if cid in Line1:
                        cust = Line1.split(',')
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
            transaction_list.append(purchase_dict)
            with open('products.txt', 'w') as outfile:
                for Line in sprodlist:
                    outfile.write(Line)
        elif add_item == 'N':
            with open('transactions.txt', 'a') as outfile1:
                outfile1.write('\n')
                outfile1.write(str(transaction_list))
            print("Purchase Successful!...")
            for key, value in purchase_dict.items():
                print(key, value)
            purchasemenu()


def purchasemenu():
    print("[1]. Search Product")
    print("[2]. Sell")
    print("[3]. Main Menu")
    print("[4]. Exit")

    selection = int(input("choose one option: "))
    while selection:
        if selection == 1:
            searchproduct()
        elif selection == 2:
            makepurchase()
        elif selection == 3:
            from main import menu
            menu()
        elif selection == 4:
            loop = 0
            print('System Exit! Goodbye...')
        else:
            print("WRONG SELECTION!")
