import sys

with open("input7.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

contains = {}
# parents = []
# for line in ins:
#    splitted = []
#    if 'shiny gold' in line:
#        splitted = line.split(' ')
#        if splitted.index('shiny') != 0 and splitted.index('gold') != 1:
#            key = splitted[0] + " " + splitted[1]
#            contains[key] = 'shiny gold'
#            #print(splitted.index('shiny'), splitted.index('gold'))
#            print(line)
#        # print(contains)


def fill_parents(child):
    parents = []
    for line in ins:
        splitted = []
        if child in line:
            splitted = line.split(' ')
            childsplit = child.split(' ')
            if splitted.index(childsplit[0]) != 0 or splitted.index(childsplit[1]) != 1:
                parent = splitted[0] + " " + splitted[1]
                parents.append(parent)
            contains[child] = parents
    for children in contains[child]:
        fill_parents(children)


# for key in contains.keys():
#    fill_parents(key)
# fill_parents('shiny gold')
fill_parents('shiny gold')
# print(contains['dark gold'])
print(len(contains.keys()))
# print(contains['striped tomato'])
# for k in contains:
# print(contains[k])
# print(contains.keys())
# print(contains)
