from Employee import Employee


def createName():
    name = input("Name: ")
    return name


def createAge():
    age = input("Age: ")
    return age


def createSalary():
    salary = int(input("Salary: "))
    return salary


if __name__ == "__main__":

    objs = list()

#    name = input("Name: ")
#    age = int(input("Age: "))
#    salary = float(input("Salary: "))

    for i in range(2):
        createObj = Employee(createName(), createAge(), createSalary())
        objs.append(createObj)


#    emp1 = Employee("Adam", 27, 3000)
#    emp2 = Employee("Jasmine", 28, 3000)

    objs[0].increment(500)

    if objs[0].higherThan(objs[1]):
        print('{} has higher salary than {}.'
              .format(objs[0].name, objs[1].name))
    else:
        print('{} has lower salary than {}.'
              .format(objs[0].name, objs[1].name))
