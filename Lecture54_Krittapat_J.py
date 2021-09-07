"""Function
Login, Menu, Selection, 1. Vat Calculation, 2. Price Calculation
User = admin   Password = 1234 """


def login():
    username_input = input("Username : ")
    password_input = input("Password : ")
    if username_input == "admin" and password_input == "1234":
        return menu()
    else:
        print("----------------")
        print("Please try again")
        print("----------------")
        return login()


def menu():
    print("Welcome to I-shop")
    print("How can i help ?")
    print("----------------")
    print("1 : VAT Calculation")
    print("2 : Price Calculation")
    return selection()


def selection():
    selected_item = input(">>> ")
    if selected_item == "1":
        return vat_calculation(int(input("Your Price : ")))
    elif selected_item == "2":
        return price_calculation()
    else:
        print("Error, Try again ")
        print("-----------------")
        return menu()


def vat_calculation(total_price):
    vat = 0.07
    result = total_price+(total_price * vat)
    return result


def price_calculation():
    first_goods = int(input("First product price : "))
    second_goods = int(input("Second product price : "))
    return vat_calculation(first_goods + second_goods)


print(login())