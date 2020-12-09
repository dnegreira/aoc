#!/usr/bin/bash
import re
import copy
with open("input4.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

fields = [
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
]

passports = [[]]
pvalid = 0
j=0


for line in ins:
    if len(line) == 0:
        j=j+1
        passports.append([])
    else:
        passports[j].append(line)

k=0

regex = r"[^|\W]([a-z]){3}:"
regex = r"(^|\s)([a-z]{3}):"

for k in range(len(passports)):
    passport = passports[k]
    print("Passport: {}".format(passports[k]))
    matches=[]
    tempmatch = copy.deepcopy(fields)
    for element in passport:
        fieldsre = re.findall(regex, element)
        for field in fieldsre:
            matches.append(field[1])
    print(matches)
    for match in matches:
        if match in tempmatch:
            tempmatch.remove(match)
    if len(tempmatch) == 0:
        pvalid=pvalid+1
        print("Valid: {}".format(passports[k]))
print(pvalid)