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

if __name__  == "__main__":
    if (len(sys.argv) < 2):
        print("use: python <pythonFile> <wordFOrSearch> [reverseIndexFile=reverse_index.json]")
        sys.exit(1)
    word = sys.argv[1]
    fileName = "reverse_index.json"
    if (len(sys.argv) > 2):
        fileName = sys.argv[2]
    pages = searchInReversedindex(word, fileName)
    print("\n".join(pages))
