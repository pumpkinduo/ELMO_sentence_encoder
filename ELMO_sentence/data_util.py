from collections import Counter
import json
import random

def get_vocab():
    sentence_vocab = []
    f = open("../PICO/trainPICO.json", 'r')
    for line in f.readlines():
        temp = json.loads(line)
        for word in temp[0]:
            sentence_vocab.append(word.lower())
    g = open("../PICO/valiPICO.json", 'r')
    for lines in g.readlines():
        temps = json.loads(lines)
        for word in temps[0]:
            sentence_vocab.append(word.lower())

    vocab = list(set(sentence_vocab))
    return vocab

def _genVocabFile(vocabFile):
    allWords = get_vocab()
    wordCount = Counter(allWords)  # 统计词频
    sortWordCount = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
    words = [item[0] for item in sortWordCount]
    allTokens = ['<S>', '</S>', '<UNK>'] + words
    with open(vocabFile, 'w') as fout:
        fout.write('\n'.join(allTokens))
    print("vocabfileget")

def get_data():
    f = open("../PICO/trainPICO.json")
    f = f.readlines()
    dataset = []
    for line in f:
        temp = json.loads(line)
        dataset.append(temp[0])
    print("数据集Get")
    return dataset

def padSentence(datasets):

    dataset = []
    inputs_length = [len(sample) for sample in datasets]
    max_source_length = max(inputs_length)

    for j,sample in enumerate(datasets):
        dataset.append(sample+[""]*(max_source_length - len(sample)))
    print("paddingget")
    return dataset


