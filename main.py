from productoperation import *
from customeroperation import *
from purchaseoperation import *
from report import *


def menu():
    loop = 1
    while loop:
        print("[1]. Customer Operations")
        print("[2]. Product Operations")
        print("[3]. Sell Operations ")
        print("[4]. Reports ")
        print("[5]. Exit")

        selection = int(input("Choose One Option: "))
        if selection == 1:
            customeroperations()

        elif selection == 2:
            productoperations()

        elif selection == 3:
            purchasemenu()

        elif selection == 4:
            reportmenu()

        elif selection == 5:
            loop = 0
            print("Goodbye")


if __name__ == '__main__':
    menu()
