Username_Input = input("Username : ")
Password_Input = input("Password : ")
if Username_Input == "admin" and Password_Input == "1234":
    print("Welcome to Dev.shop")
    print("----------Item List----------")
    print(1, "keyboard     : 1500 THB")
    print(2, "Mouse        :  800 THB")
    print(3, "Power Supply : 2500 THB")
    print(4, "Monitor      : 5000 THB")
    print("-----------------------------")
    Product = int(input("Press select your Product : "))
    if Product == 1:
        Price = 1500
        Amount = int(input("How many ? : "))
        print("-----------------------------")
        print("Your selected product >> Keyboard")
        print("Your total expenses : ", Price * Amount, "THB")
    elif Product == 2:
        Price = 800
        Amount = int(input("How many ? : "))
        print("-----------------------------")
        print("Your selected product >> Mouse")
        print("Your total expenses : ", Price * Amount, "THB")
    elif Product == 3:
        Price = 2500
        Amount = int(input("How many ? : "))
        print("-----------------------------")
        print("Your selected product >> Power Supply")
        print("Your total expenses : ", Price * Amount, "THB")
    elif Product == 4:
        Price = 5000
        Amount = int(input("How many ? : "))
        print("-----------------------------")
        print("Your selected product >> Monitor")
        print("Your total expenses : ", Price * Amount, "THB")
    else:
        print("There's no item")
else:
    print("Your username and/or password are incorrect")



