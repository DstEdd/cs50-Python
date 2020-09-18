import csv
from sys import argv

if len(argv) != 3:
    print("Pls, provide db and sequence as command-line-arg!")
    exit(1)

sqnc = ""
STRs = []
people = {}

with open(argv[1], "r") as database, open(argv[2], "r") as sequence:
    sqnc = sequence.read()
    db_reader = csv.reader(database)

    for row in db_reader:
        if row[0] == "name":
            STRs = row.copy()[1:]
        else:
            people[row[0]] = [int(i) for i in row[1:]]

str_repeats = []
for str in STRs:
    i = 0
    max_reps = 0
    curr_max_reps = 0
    while i < len(sqnc):
        curr_thunk = sqnc[i:i + len(str)]
        if curr_thunk == str:
            curr_max_reps += 1
            max_reps = max(curr_max_reps, max_reps)
            i += len(str)
        else:
            curr_max_reps = 0
            i += 1
    str_repeats.append(max_reps)

for name, strs in people.items():
    if strs == str_repeats:
        print(name)
        exit(0)

print("No Match")