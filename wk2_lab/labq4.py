def enterSales(x):
    y = []
    for i in range(3):
        if (i == 0):
            userInput = int(input("Enter Sales for Sunday's Dried noodle: "))
            y.append(userInput)
        elif (i == 1):
            userInput = int(input("Enter Sales for Sunday's Dark noodle: "))
            y.append(userInput)
        else:
            userInput = int(input("Enter Sales for Sunday's Spicy noodle: "))
            y.append(userInput)

    y.append(y[0] + y[1] + y[2])
    x.append(y)
    return x


def totalWeeklySales(x):
    total = 0
    for i in range(len(x)):
        total = total + x[i][3]

    return total


if __name__ == "__main__":
    sales = [[380, 100, 240, 720],
             [300, 200, 300, 800],
             [250, 240, 130, 620],
             [320, 150, 200, 670],
             [200, 200, 200, 600],
             [400, 300, 290, 990]]

    sales = enterSales(sales)
    print("Total sales of the week RM{:.2f}".format(
        totalWeeklySales(sales)))
