import os
import csv

words = []
tags =  []

with open('language-tags-4.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

for row in data:
    words.append(row[0])
    tags.append(row[1])

nReplacements = [0] * len(words)

text_dir = '../epub/text'
for file in os.listdir(text_dir):
    filename = os.fsdecode(file)
    lines = []
    with open(os.path.join(text_dir, filename)) as infile:
        for line in infile:
            for i in range(0, len(words)):
                nReplacements[i] += line.count("<i>" + words[i] + "</i>")
                line = line.replace("<i>" + words[i] + "</i>", "<i xml:lang=\"" + tags[i] + "\">" + words[i] + "</i>")
            lines.append(line)
    with open(os.path.join(text_dir, filename), 'w') as outfile:
        for line in lines:
         outfile.write(line)

for i in range(0, len(words)):
    print(words[i] + ": " + tags[i] + " (" + str(nReplacements[i]) + ")")