
ids = []
with open("input5.txt") as f_in:
    ins = [_.strip() for _ in f_in.readlines()]

for line in ins:
    row = "0b"
    column = "0b"
    for i in line:
        if i == "B":
            row = row + "1"
        if i == "F":
            row = row + "0"
        if i == "R":
            column = column + "1"
        if i == "L":
            column = column + "0"
    ids.append(int(row, 2) * 8 + int(column, 2))

minid = min(ids)

for seatid in range(minid, len(ids)):
    try:
        ids.index(seatid)
    except ValueError:
        print("Seatid missing: {}".format(seatid))

print(max(ids))
