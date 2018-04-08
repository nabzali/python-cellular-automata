while True:
    try:
        num_gens = int(input("Please enter a number of generations:\n"))
        if num_gens > 100:
            print("You have entered a number greater than 10. Try again.")
            continue
        elif num_gens < 1:
            print("You have entered a number lower than 1. Try again.")
        else:
            break
    except ValueError:
        print("This must be an integer (not larger than 10). Try Again.")


while True:  # Error checking for input of rule (8 bit integer)
    try:
        user_rule = str(input("Please enter a rule:\n"))
        isBinary = True
        for i in str(user_rule):
            if i not in ["0", "1"]:
                print("You must enter a binary number. Try again.")
                isBinary = False
                break
        if not isBinary:
            continue
        if len(str(user_rule)) != 8:
            print("Rule must be 8 digits long (one byte).")
            continue
        break
    except ValueError:
        print("You must enter a number (must also be binary). Try again.")

