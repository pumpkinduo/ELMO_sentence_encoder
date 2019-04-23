import csv
import codecs
datasets = []

f = open("PICO_test.txt")


i = 0
count = 0
g = f.readlines()
for line in g:

    if line != "" and line != "\n":
        count += 1
        file = "".join(g).split("\n\n")
        all_sentence = []
        # print(i)

        for lines in file[i].split("\n"):
            if not lines.startswith("###"):
                ls2 = lines.split("|")
                sentencess = ls2[2:]
                sentencess = "".join(sentencess).strip().split(" ")
                for word in sentencess:
                    if word != "":
                        all_sentence.append(word)

        if count > len(file[i].split("\n")):
            i += 1
            count = 0

        dataset = []
        sentencelist = []
        if not line.startswith("###"):
            line = "".join(line)
            ls = line.split("|")
            tag, sentence = ls[1], ls[2:]
            sentence = "".join(sentence).strip()
            sentence = sentence.split(" ")
            for word in sentence:
                sentencelist.append(word)
            dataset.append(sentencelist)
            dataset.append(tag)
            dataset.append(all_sentence)
            datasets.append(dataset)


for j in datasets:
    if j[0] == [""]:
        datasets.remove(j)

print("数据加载完毕")
import json
with open("../PICO/testPICO.json","w",encoding="utf-8") as f:
    for index,word in enumerate(datasets):
        json.dump(datasets[index], f)
        f.write("\n")
