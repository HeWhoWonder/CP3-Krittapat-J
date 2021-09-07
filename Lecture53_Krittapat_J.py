def vat_calculator(total_price):
    result = total_price + (total_price * 0.07)
    return result


print("net = ", vat_calculator(float(input("Your price : "))), "THB")
