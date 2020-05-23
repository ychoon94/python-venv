from Employee import Employee


def createobject(name, age, salary):
    objs = [Employee(name, age, salary) for i in range(10)]
    return objs

if __name__ == "__main__":

    objs = createobject("Jasmine", 28, 3000)
    createobject("Adam", 27, 3000)

    print(objs[0].salary)

#    emp1 = Employee("Adam", 27, 3000)
#    emp2 = Employee("Jasmine", 28, 3000)

    objs[0].increment(500)

    if objs[0].higherThan(objs[1]):
        print('Adam has higher salary than Jasmine.')
    else:
        print('Adam has lower salary than Jasmine.')
