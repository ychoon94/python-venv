if __name__ == "__main__":
    test = []
    for i in range(10):
        try:
            number = int(input("insert a number: "))
            print(number)
            test.append(number)
        except ValueError:
            print("wrong input!")
    print(test)
