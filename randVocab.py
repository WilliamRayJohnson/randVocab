'''
A script that prints random japanese vocab words from a file and prints
them to screen.
'''

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

    for word in vocab:
        print(word)

if __name__ == '__main__':
    main()
