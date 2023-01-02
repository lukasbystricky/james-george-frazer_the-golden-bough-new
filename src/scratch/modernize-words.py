import os
import csv

oldWords = []
newWords =  []

with open('modernizations-4.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

for row in data:
    oldWords.append(row[0])
    newWords.append(row[1])

nReplacements = [0] * len(oldWords)

text_dir = '../epub/text'
for file in os.listdir(text_dir):
    filename = os.fsdecode(file)
    lines = []
    with open(os.path.join(text_dir, filename)) as infile:
        for line in infile:
            for i in range(0, len(oldWords)):
                nReplacements[i] += line.count(oldWords[i])
                line = line.replace(oldWords[i], newWords[i])
            lines.append(line)
    with open(os.path.join(text_dir, filename), 'w') as outfile:
        for line in lines:
         outfile.write(line)

for i in range(0, len(oldWords)):
    print(oldWords[i] + " -> " + newWords[i] + " (" + str(nReplacements[i]) + ")")

# Add new words to the dictionary
lines = []
with open('custom-dictionary-golden-bough.txt') as dict:
    for line in dict:
        lines.append(line)
    for i in range(0, len(newWords)):
        txt = newWords[i].split(" ")
        for j in range(0, len(txt)):
            lines.append(txt[j] + "\n")

with open('custom-dictionary-golden-bough.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line)