def trackLift(counter):
    if counter != 0 and counter > 0:
        print("Lift stops at level {}".format(counter))
        counter -= 1
        trackLift(counter)
    elif counter < 0 and counter != -6:
        print("Lift up level {}".format(-(counter)))
        counter -= 1
        trackLift(counter)
    elif counter == 0:
        print("Lift takes a break at lobby ground floor")
        counter = -1
        trackLift(counter)


trackLift(5)
