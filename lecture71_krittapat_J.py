menu_list = []
price_list = []


def menu_preview():
    total_price = 0
    print("----Menu Preview----")
    for number in range(len(menu_list)):
        print(menu_list[number], price_list[number], "THB")
        total_price += int(price_list[number])
    print("Total =", total_price, "THB")


while True:
    menu = input("Please enter your menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("How much ? : "))
        menu_list.append(menu)
        price_list.append(price)
menu_preview()
