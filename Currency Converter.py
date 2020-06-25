money = {"$": {"€": 0.9, "£": 0.77, "₺": 5.94, "﷼": 3.75}, "£": {"€": 1.17, "$": 1.30, "₺": 7.72, "﷼": 4.88},"€": {"$": 1.11, "£": 0.85, "₺": 6.58, "﷼": 4.16}, "₺": {"€": 0.15, "£": 0.13, "$": 0.17, "﷼": 0.63},"﷼": {"€": 0.24, "£": 0.2, "₺": 1.58, "$": 0.27}}
symbol = {"dolar": "$", "euro": "€", "pound": "£", "tl": "₺", "riyal" : "﷼"}
def currency():
    while True:
        fromType = input("Which currency you want to covert from?: ")
        print("")
        try: fromType = symbol[fromType]
        except KeyError: print("Invalid currency. Please enter again\n")
        else: break
    while True:
        toType = input("Which currency you want to covert to?: ")
        print("")
        try: toType = symbol[toType]
        except KeyError: print("Invalid currency. Please enter again\n")
        else: break
    while True:
        try: number = float(input("How much you want to covert: "))
        except ValueError as hata1: print("\nYou need to enter a number. Please try again\n")
        else: break
    converted = number * money[fromType][toType]
    converted = float("{:.2f}".format(converted))
    print(f"\n{converted}\n")
    while True:
        ans = input("Do you want to make another operation? (y or n): ").upper()
        if ans == "Y": currency()
        elif ans == "N": exit()
        else: print("Your answer should be y or n. Please enter again\n")
currency()