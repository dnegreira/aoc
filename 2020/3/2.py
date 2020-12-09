#!/usr/bin/python3

with open("input3.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

def custom_path(r, d):
    marker = 0
    trees = 0
    for i in range(0,len(ins)-1,d):
        if i == 0 or len(ins[i]) <= 1:
            continue
        marker+=r
        if marker > len(ins[i])-1:
            marker = marker - len(ins[i])
        if ins[i][marker] == "#":
            trees+=1
        i+=d
    return trees

results = []
results.append(int(custom_path(1,1)))
results.append(int(custom_path(3,1)))
results.append(int(custom_path(5,1)))
results.append(int(custom_path(7,1)))
results.append(int(custom_path(1,2)))

total=1
for r in results:
    total = total * r

print(results)
print("Total is: {}".format(total))