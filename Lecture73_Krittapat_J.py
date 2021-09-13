menu_list = {'ข้าวมันไก่': 40, 'หมูสามชั้น': 60, 'ข้าวผัด': 50, 'บัวลอย': 15}
customer_list = []


def preview():
    total_price = 0
    print("Summary".center(65, "-"))
    for number in range(len(customer_list)):
        print(customer_list[number][0], customer_list[number][1])
        total_price += customer_list[number][1]
    print("Total", total_price, "THB")


print("menu".center(65, "-"))
print(menu_list, "or exit ")
while True:
    customer_input = input("What would you like to eat :")
    if customer_input == 'exit':
        break
    else:
        customer_list.append([customer_input, menu_list[customer_input]])

preview()
