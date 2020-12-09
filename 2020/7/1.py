from collections import defaultdict
with open("input7.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

contains = {}
multiplier = 0


def fill_bags(parent):
    children = []
    for line in ins:
        splitted = []
        if parent in line:
            splitted = line.split(' ')
            parentsplit = parent.split(' ')
            if splitted.index(parentsplit[0]) == 0 and splitted.index(parentsplit[1]) == 1:
                firstchild = []
                parent = splitted[0] + " " + splitted[1]
                splittedchild = line.split('contains')
                firstchild = splittedchild[0].split('contain')[1]
                if "other bags" in firstchild:
                    continue
                for child in firstchild.split(","):
                    print(child)
                    children.append(child.lstrip())
            contains[parent] = children
    for children in contains[parent]:
        split_childs = children.split(',')
        for child in split_childs:
            nospacechild = child.lstrip()
            childsplit = nospacechild.split(" ")
            child_name = childsplit[1] + " " + childsplit[2]
            fill_bags(child_name)


fill_bags('shiny gold')


def calculate_bags(bag):
    total = 0
    for v in contains[bag]:
        if len(v) > 0:
            splitv = v.split(" ")
            number = int(splitv[0])
            bag_name = splitv[1] + " " + splitv[2]
            total += number + (number * calculate_bags(bag_name))
    return total


print(calculate_bags("shiny gold"))
