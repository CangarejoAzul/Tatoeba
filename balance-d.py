from sys import argv
from random import shuffle
from re import findall

print("Reading dictionary...")
input = open(argv[2], encoding = "utf-8")
dictionary = {}
for line in input:
  split = findall("[^\t\n]+", line)
  if len(split[0]) not in dictionary:
    dictionary[len(split[0])] = {}
  dictionary[len(split[0])][split[0].lower()] = set()

print("Sorting sentences...")
input = open(argv[3], encoding = "utf-8")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[1] == argv[1]:
    sentence = split[2].lower()
    for length in dictionary:
      for i in range(len(split[2].lower()) - length + 1):
        if split[2].lower()[i : i + length] in dictionary[length]:
          dictionary[length][split[2].lower()[i : i + length]].add(split[0])
for length in dictionary:
  for word in dictionary[length]:
    dictionary[length][word] = list(dictionary[length][word])
    shuffle(dictionary[length][word])

print("Writing sentences...")
sentences = set()
for length in dictionary:
  for word in dictionary[length]:
    sentences.update(dictionary[length][word][:10])
input = open(argv[3], encoding = "utf-8")
output = open(argv[4], "w", encoding = "utf-8")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] in sentences:
    print(line, end = "", file = output)

print("Done!")
