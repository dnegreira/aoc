#!/usr/bin/python3

f = open("input1.txt")

inputf = []
for line in f:
    inputf.append(line.rstrip())

iterations = 0
for i in inputf:
    iterations+=1
    el = inputf.index(i)
    for j in inputf[el:]:
        iterations+=1
        if int(i) + int(j) == 2020:
            print("Result is: {}".format(int(i) * int(j)))
            print("Iterations: {}".format(iterations))