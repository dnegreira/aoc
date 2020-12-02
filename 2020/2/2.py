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
    if password[count[0]-1] == letter and password[count[1]-1] != letter:
        match += 1
    elif password[count[0]-1] != letter and password[count[1]-1] == letter:
        match += 1

print("Number of matches: {}".format(match))
