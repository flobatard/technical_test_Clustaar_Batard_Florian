import blacklist
import json

def setOfWordsFromText(text, ignores, separators):
    setOfWords = set()



class ReverseIndex:

    def __init__(self, wordsFilename, ignores = ['.', ',', ';'], separators=[' ', '\n','\t']):
        self.bl = blacklist.BlackList(wordsFilename)
        self.reverseindex = {}
        self.ignores = ignores
        self.separators = separators

    def feedFromfile(self, articleJsonFile):
        f = open(articleJsonFile, encoding='utf-8')
        article = json.load(f)
        f.close()
        self.feedSingle(article)


    def feedFromMultipleFile(self, articleJsonFiles):
        for articleJsonFile in articleJsonFiles:
            self.feedFromfile(articleJsonFile)

    def feedMultiple(self, articleList):
        for article in articleList:
            self.feedSingle(article)

    def feedSingle(self, article):
        setTitle = self.setOfWordsFromText(article.title)
        setContent = self.setOfWordsFromText(article.content)
        finalWordSet = setTitle.union(setContent)
        for word in finalWordSet:
            try:
                self.reverseindex[word].append(article.pageName)
            except KeyError as e:
                self.reverseindex[word] = [article.pageName]


    def setOfWordsFromText(self, text):
        tmpText = text
         #Remove the caracter to ignore that can disturb the parsing of words
        for ignore in self.ignores:
            tmpText.replace(ignore, '')
        
        #Convert all separators into a single one ' '
        for separator in self.separators:
            tmpText.replace(separator, ' ')
        
        #Split
        words = tmpText.split(' ')
        
        finalWords = []
        #Remove empty string '' and quotes around words
        for word in words:
            newWord = word.strip("'")
            if (self.bl._is_blacklisted(newWord)):
                finalWords.append(newWord)

        
        return set(finalWords)

    def to_json(self, fileName):
        f = open(fileName, encoding='utf-8', mode='w')
        f.write(json.dumps(self.reverseindex, indent=4))
        f.close()
