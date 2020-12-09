with open("input8.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]
accumulator = 0
i = 0
operationsdone = []


def operation(op, arg):
    global accumulator
    global i
    if op == "acc":
        accumulator = accumulator + arg
        i += 1
    if op == "jmp":
        i = i+arg
    if op == "nop":
        i += 1
    return True


while True:
    action = ins[i].split(" ")
    operation(action[0], int(action[1]))
    if i in operationsdone:
        print("Accumulator: {}".format(accumulator))
        break
    operationsdone.append(i)
    print(operationsdone)
    print(i)
