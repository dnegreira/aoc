#!/usr/bin/python3

trees = 0

marker = 0
with open("input3.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]
    for i in range(len(ins)-1):
        if i == 0 or len(ins[i]) <= 1:
            i+=1
            continue
        marker+=3
        if marker > len(ins[i])-1:
            marker = marker - len(ins[i])
        if ins[i][marker] == "#":
            trees+=1
        i+=1
print(trees)