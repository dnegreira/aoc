#!/usr/bin/python3

f = open("input1.txt")

inputf = []
for line in f:
    inputf.append(int(line.rstrip()))

iterations = 0
for i in inputf:
    iterations+=1
    el = inputf.index(i)
    for j in inputf[el:]:
        iterations+=1
        ek = inputf.index(j)
        for k in inputf[ek:]:
            iterations+=1
            if i + j + k == 2020:
                print("Result is: {}".format(int(i) * int(j) * int(k)))
                print("Iterations: {}".format(iterations))
#                exit()
