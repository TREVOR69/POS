
def menu():
    print("[1]. Customer Operations")
    print("[2]. Product Operations")
    print("[3]. Reports")
    print("[0]. Exit")


menu()
selection = int(input("Choose One Option: "))

while selection != 0:
    if selection == 1:
        customeroperation()
        #print("option 1 selected. ")
    elif selection == 2:
        #productoperation()
        print("option 2 selected. ")
    elif selection == 3:
        #reports()
        print("option 3 selected. ")
    menu()
    selection = int(input("choose one option"))

print("Goodbye")