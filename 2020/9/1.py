with open("input9.txt") as f_in:
    ins = [int(_.strip()) for _ in f_in.readlines()]

preamble = 25
gocheck = 0
total = 0


def check_sum(one, two, check):
    if one+two == check:
        return True
    else:
        return False


for i in range(preamble, len(ins)):
    sequence = ins[i-preamble:i]
    numcheck = ins[i]
    checks = []
    for j in range(len(sequence)):
        num = sequence[j]
        for k in sequence:
            if k != num:
                if check_sum(num, k, numcheck):
                    checks.append(True)
                    break
    if True not in checks:
        print("Numcheck: {}".format(numcheck))
        gocheck = numcheck

for i in range(ins.index(gocheck)):

    checking = ins[0: i]
    for j in range(len(checking), 0, -1):
        total = sum(checking[j:len(checking)])
        if total == gocheck:
            minimum = min(checking[j:len(checking)])
            maximum = max(checking[j:len(checking)])
            print("answer: {}".format(minimum + maximum))
