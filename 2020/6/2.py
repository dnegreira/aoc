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
    answerdict = {}
    answercount = []

    [answerlist.append(reply) for reply in answer]
    
    groups = len(answerlist)
    unique = set("".join(answerlist))

    answerdict = answerdict.fromkeys(unique, 0)
    
    for x in answerlist:
        for c in x:
            answerdict[c] = answerdict[c] + 1
    
    [ answercount.append(1) for value in answerdict.values() if value == groups]

    for answer in answercount:
        if type(answer) == int:
            total = total+1
    print(answercount)
    
print(total)