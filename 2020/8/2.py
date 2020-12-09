with open("input8.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]
accumulator = 0
i = 0
j = 0
operationsdone = []


def operation(op, arg):
    global accumulator
    global i
    #print("Operation: {} {}".format(op, arg))
    if op == "acc":
        accumulator = accumulator + arg
        i += 1
    if op == "jmp":
        i = i+arg
    if op == "nop":
        i += 1
    return True


def check_loop():
    while True:
     #   print(i)
        action = modified[i].split(" ")
        operation(action[0], int(action[1]))
        if i in operationsdone or i < 0:
          #      print(
          #          "Operation repeated/negative: i: {} operations done: {}".format(i, operationsdone))
            break
        # if i == len(modified):
        #    print("Finished: {}".format(accumulator))
        if i == len(modified):
            print("boop: {}".format(accumulator))
            exit
        if i > len(modified):
            #    print("Ran through the whole file: Accumulator: {}".format(accumulator))
            break

        operationsdone.append(i)


for line in ins:
    #print("Next line")
    i = 0
    accumulator = 0
    operationsdone = []
    modified = ins.copy()
    action = ins[j].split(" ")
    if action[0] == "jmp":
        modified[j] = "nop " + action[1]
        check_loop()
    if action[0] == "nop":
        modified[j] = "jmp " + action[1]
        check_loop()
    else:
        check_loop()
    j += 1
