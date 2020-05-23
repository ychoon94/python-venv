cost_price = []
i = 0

while i < 10:
    userInput = float(input("Enter price: "))

    if (userInput >= 0 and userInput <= 1000):
        cost_price.append(userInput)
        i += 1
    else:
        print("invalid input")
        i = i

price_with_tax = []
tax = 1.06

for j in range(len(cost_price)):
    cost = cost_price[j] * tax
    price_with_tax.append(cost)

for k in range(len(cost_price)):
    print("Unit {0:<3}:    cost price: {1:<10.2f} price with tax: {2:<10.2f}".format(
        k + 1, cost_price[k], price_with_tax[k]))
