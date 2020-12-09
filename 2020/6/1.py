#!/usr/bin/python3

answers = [[]]
j=0
k=0
answernumber = []
total = 0
with open("input6.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

for line in ins:
    if len(line) == 0:
        j=j+1
        answers.append([])
    else:
        answers[j].append(line)

for k in range(len(answers)):
    answer = answers[k]
    answerlist = []
    unique = []
    for reply in answer:
        answerlist.append(reply)
    for x in answerlist:
        for c in x:
            if c not in unique:
                unique.append(c)
    print(unique)
    answernumber.append(len(unique))

for number in answernumber:
    total = total + number

print(total)

