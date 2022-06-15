def reportmenu():
    print("[1].Search Customer")
    print("[2].Show all products")
    print("[3].Show all customers")
    print("[4].Search purchase transaction")
    print("[5].Main Menu")

    selection = int(input("choose one option: "))
    while selection:
        if selection == 1:
            searchcustomer()
        elif selection == 2:
            showallproducts()
        elif selection == 3:
            showallcustomers()
        elif selection == 4:
            searchtransaction()
        elif selection == 5:
            from main import menu
            menu()
        else:
            print("WRONG SELECTION!")


def searchcustomer():
    lt = []
    with open("customer.txt", "r") as z:
        pid = int(input("Enter Customer Id: "))
        for Line in z:
            if str(pid) in Line:
                lt.append(Line)
                print(lt)
                reportmenu()


def showallproducts():
    with open("products.txt", "r") as z:
        t = z.readlines()
        for Lines in t:
            print(Lines)
            break
            #reportmenu()


def showallcustomers():
    lt = []
    with open("customer.txt", "r") as z:
        t = z.readlines()
        for Lines in t:
            print(Lines)
            reportmenu()


def searchtransaction():
    transid = input("Enter Transaction id: ")
    with open("transactions.txt", "r") as p:
        q = p.readlines()
        for lines in q:
            if transid in lines:
                print(lines)
                reportmenu()
