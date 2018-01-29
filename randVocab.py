#!/usr/bin/python3

'''
A script that prints random japanese vocab words from a file and prints
them to screen.
'''

import numpy as np
import os

def getVocab(filename):
    vocab = []
    vocabFile = open(filename, 'r', encoding="utf-8")

    for line in vocabFile:
        vocab.append(line)

    vocabFile.close()
    return vocab

def main():
    vocabFilename = "genkiVerbs.txt"

    vocab = getVocab(vocabFilename)
    vocab = np.random.choice(vocab, len(vocab), replace=False)

    for word in vocab:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(word)
        input()
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
