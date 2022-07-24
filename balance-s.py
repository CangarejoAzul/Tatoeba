from sys import argv
from random import shuffle
from re import findall

print("Sorting sentences...")
input = open(argv[2], encoding = "utf-8")
dictionary = {}
for line in input:
  split = findall(r"[^\t\n]+", line)
  if split[1] == argv[1]:
    for word in findall(r"\w+", split[2].lower()):
      if word not in dictionary:
        dictionary[word] = set()
      dictionary[word].add(split[0])
for word in dictionary:
  dictionary[word] = list(dictionary[word])
  shuffle(dictionary[word])

print("Writing sentences...")
sentences = set()
for word in dictionary:
  sentences.update(dictionary[word][:10])
input = open(argv[2], encoding = "utf-8")
output = open(argv[3], "w", encoding = "utf-8")
for line in input:
  split = findall(r"[^\t\n]+", line)
  if split[0] in sentences:
    print(line, end = "", file = output)

print("Done!")
