#!/usr/bin/python3

from os import SCHED_OTHER
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


def validator(field, value):
    if field == "byr" and int(value) >=1920 and int(value) <= 2002:
        return True
    if field == "iyr" and int(value) >=2010 and int(value) <=2020:
        return True
    if field == "eyr" and int(value) >=2020 and int(value) <= 2030:
        return True
    if field == "hgt":
        regex = r"([0-9]{2,3})(.*)"
        measures = re.findall(regex, value)
        if measures[0][1] == "cm" and int(measures[0][0]) >=150 and int(measures[0][0]) <=193:
            return True
        if measures[0][1] == "in" and int(measures[0][0]) >=59 and int(measures[0][0]) <=76:
            return True
    if field == "hcl":
        regex = r"#[0-9a-f]{6}($|\s)"
        color = re.findall(regex, value)
        if len(color) > 0:
            return True
    if field == "ecl":
        validv = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value in validv:
            return True
    if field == "pid":
        regex = r"^[0-9]{9}($|\s)"
        findpid = re.search(regex, value)
        if findpid != None:
            return True
    if field == "cid":
        return True
    return False

for line in ins:
    if len(line) == 0:
        j=j+1
        passports.append([])
    else:
        passports[j].append(line)

k=0

regexf = r"(^|\s)([a-z]{3}):"
regexfv = r"(^|\s)([a-z]{3}):([#a-z0-9]*)"

for k in range(len(passports)):
    passport = passports[k]
    matches=[]
    validated = []

    tempmatch = copy.deepcopy(fields)
    for element in passport:
        fieldsre = re.findall(regexf, element)
        for field in fieldsre:
            matches.append(field[1])
    for match in matches:
        if match in tempmatch:
            tempmatch.remove(match)
    if len(tempmatch) == 0:
        for element in passport:
            fieldsvre = re.findall(regexfv, element)
            for field in fieldsvre:
                validated.append(validator(field[1], field[2]))
        if False not in validated:
            pvalid=pvalid+1

print(pvalid)