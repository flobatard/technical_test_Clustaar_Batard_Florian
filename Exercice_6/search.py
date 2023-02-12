import json
import sys

def searchInReversedindex(word, filePath):
    f = open(filePath, encoding='utf-8')
    reversedIndex = json.load(f)
    f.close()
    ret = []
    try:
        ret = reversedIndex[word]
    except KeyError as e:
        print("Aucune page ne correspond à votre recherche")
    return ret

def searchInReversedSentenceindexOR(words, filePath):
    f = open(filePath, encoding='utf-8')
    reversedIndex = json.load(f)
    f.close()
    ret = set()
    for word in words:
        try:
            ret = ret.union(set(reversedIndex[word]))
        except KeyError:
            print("Not found: ", word)
            pass
    return ret

def searchInReversedSentenceindexAND(words, filePath):
    f = open(filePath, encoding='utf-8')
    reversedIndex = json.load(f)
    f.close()
    ret = set()
    init = True
    for word in words:
        try:
            if (init):
                ret = set(reversedIndex[word])
                init = False
            else:
                ret = ret.intersection(set(reversedIndex[word]))
        except KeyError:
            print("Not found: ", word)
            pass
    return ret


if __name__  == "__main__":
    
    if (len(sys.argv) < 2):
        print("use: python <pythonFile> <wordFOrSearch> [reverseIndexFile=reverse_index.json]")
        sys.exit(1)
    sentence = sys.argv[1]
    fileName = "reverse_index.json"
    sentence.replace(',',' ')
    sentence.replace('.', ' ')
    words = sentence.split(' ')
    if (len(sys.argv) > 2):
        fileName = sys.argv[2]
    pages = searchInReversedSentenceindexOR(words, fileName)
    print("\n".join(pages))
