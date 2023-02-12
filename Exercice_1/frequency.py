import blacklist as bl
import sys


class Frequency:

    def __init__(self, textFilename, wordsFilename, ignores = ['.', ',', ';'], separators=[' ', '\n','\t']):
        self.blacklist = bl.BlackList(wordsFilename)
        f = open(textFilename, encoding="utf-8")
        self.text = f.read()
        self.ignores = ignores
        self.separators = separators
        f.close()
    
    def _is_word_meaningful(self, word):
        return self.blacklist._is_blacklisted(word)

    def _compute_frequencies(self):
        tmp = self.text
        
        #Remove the caracter to ignore that can disturb the parsing of words
        for ignore in self.ignores:
            tmp.replace(ignore, '')
        
        #Convert all separators into a single one ' '
        for separator in self.separators:
            tmp.replace(separator, ' ')
        
        #Split
        words = tmp.split(' ')

        # Remove quotes for words that are one quotes Ex: 'gros-nez'
        for i in range(len(words)):
            words[i] = words[i].strip("'")

        #Dict who will get frequencies {word : occurences}
        all_frequency = {}
        #Computation
        for word in words:
            try:
                if (self._is_word_meaningful(word)):
                    all_frequency[word] = all_frequency[word]+1
            except KeyError as e:
                all_frequency[word] = 1

        #Sorted list of frequencies
        sortedFrequency = sorted(all_frequency.items(), key=lambda x : -x[1])
    
        return sortedFrequency


if __name__=='__main__':
    textFilename = 'texte.txt'
    if (len(sys.argv) > 1):
        textFilename = sys.argv[1]
    wordsFilename = 'words.txt'
    if (len(sys.argv) > 2):
        wordsFilename = sys.argv[2]
    
    frequency = Frequency(textFilename, wordsFilename)
    frequencies = frequency._compute_frequencies()
    print(frequencies[:10])