def generate(n, rule):
    automata = []
    user_rule_arr = [] # [rule[0], rule[1] ...etc] --> e.g: [1,0,1,0,1,0] if say rule was 101010

    for j in rule: #Appends each digit of the rule to an array #THIS IS WHAT DOESNT FKING WORK
        user_rule_arr.append(int(j)) #Appends each digit of rule to an array, which becomes the first element of automata multi-dimensional array
    #LOOP ABOVE WAS CAUSING ME PROBLEMS - SIMPLE ERROR WAS I USED i variable instead of j
    automata.append([0,0,0,0,1,0,0,0,0]) #Automata array holds its first element, the first generation
    for k in range(0, n-1): #Loop that creates each generation, appending them to automata
        current = automata[k]
        new = []

        for l in range(0, 9): #loop that considers each neighbourhood and generates the next current
            mid = current[l]
            if l == 0:
                left = current[8]
                right = current[1]
            elif l == 8:
                left = current[7]
                right = current[0]
            else:
                left = current[l-1]
                right = current[l+1]
            index = str(left)+str(mid)+str(right)
            if index == "000":
                new_num = user_rule_arr[0]
            elif index == "001":
                new_num = user_rule_arr[1]
            elif index == "010":
                new_num = user_rule_arr[2]
            elif index == "011":
                new_num = user_rule_arr[3]
            elif index == "100":
                new_num = user_rule_arr[4]
            elif index == "101":
                new_num = user_rule_arr[5]
            elif index == "110":
                new_num = user_rule_arr[6]
            else:
                new_num = user_rule_arr[7]
            new.append(new_num)
        string = ""

        for m in new:
            if m == 1:
                string += "  *  "
            else:
                string += "     "
        print(string)

        automata.append(new)
    #print(automata)
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
        print("This must be an integer (not larger than 100). Try Again.")


while True:  # Error checking for input of rule (8 bit integer)
    user_rule = str(input("Please enter a rule:\n"))
    isBinary = True
    for i in user_rule:
        if i not in ["0", "1"]:
            print("You must enter a binary number. Try again.")
            isBinary = False
            break
    if not isBinary:
        continue
    if len(user_rule) != 8:
        print("Rule must be 8 digits long (one byte).")
        continue
    break

generate(num_gens, user_rule)
