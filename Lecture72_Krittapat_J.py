menu_list = []


def menu_preview():
    total_price = 0
    print("----Menu Preview----")
    for number in range(len(menu_list)):
        print(menu_list[number][0], menu_list[number][1], "THB")
        total_price += int(menu_list[number][1])
    print("Total =", total_price, "THB")


while True:
    menu = input("Please enter your menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("How much ? : "))
        menu_list.append([menu, price])
print(menu_list)
menu_preview()
