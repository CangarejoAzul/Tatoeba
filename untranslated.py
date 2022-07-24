from sys import argv
from re import findall

input = open(argv[3], encoding="utf-8")
adjacency = {}
print("Reading links...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] not in adjacency:
    adjacency[split[0]] = []
  adjacency[split[0]].append(split[1])

input = open(argv[4], encoding="utf-8")
output = open(argv[5], "w")
print("Writing adjacency...")
for line in input:
  split = findall("[^\t\n]+", line)
  print(split[0], end = "", file = output)
  if split[0] in adjacency:
    for id1 in adjacency[split[0]]:
      print("\t", id1, sep = "", end = "", file = output)
      for id2 in adjacency[id1]:
        print("\t", id2, sep = "", end = "", file = output)
  print("\n", end = "", file = output)

del adjacency

input = open(argv[4], encoding="utf-8")
language = {}
print("Reading languages...")
for line in input:
  split = findall("[^\t\n]+", line)
  language[split[0]] = split[1]

input = open(argv[5], encoding="utf-8")
untranslated = set()
print("Finding untranslated...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] in language and language[split[0]] == argv[1] and all(id not in language or language[id] != argv[2] for id in split):
    untranslated.add(split[0])

input = open(argv[4], encoding="utf-8")
output = open(argv[6], "w", encoding="utf-8")
print("Writing untranslated...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] in untranslated:
    print(line, end = "", file = output)

print("Done!")
