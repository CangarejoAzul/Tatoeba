from sys import argv
from re import findall

print("Reading languages...")
input = open(argv[1], encoding = "utf-8")
languages = {}
for line in input:
  split = findall("[^\t\n]+", line)
  if len(split) >= 3 and split[1] == "5":
    if split[2] not in languages:
      languages[split[2]] = set()
    languages[split[2]].add(split[0])

print("Filtering native...")
input = open(argv[2], encoding = "utf-8")
output = open(argv[3], "w", encoding = "utf-8")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[3] in languages and split[1] in languages[split[3]]:
    print(line, end = "", file = output)

print("Done!")
