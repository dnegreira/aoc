#!/usr/bin/python3

f = open("input2.txt")

match = 0
for line in f:
    count = []
    inputl = line.split()
    for i in inputl[0].split("-"):
        count.append(int(i))
    letter = inputl[1][0]
    password = inputl[2]
    if password.count(letter) >= count[0] and password.count(letter) <= count[1]:
        match += 1

print("Number of matches: {}".format(match))
