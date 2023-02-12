import html
import html.parser
import sys
from bs4 import BeautifulSoup

class HTML_Article_Parser:

    

    def __init__(self):
        self.htmlText = ''
        self.parsing = ''
        self.lastTag = []
        self.title = ''
        self.content = ''
        self.footer = ''
        self.links = []
        

    def fromFile(self, filename):
        self.clear()
        f = open(filename, encoding='utf-8')
        self.htmlText = f.read()
        f.close()

    def fromHtmlText(self, htmlText):
        self.clear()
        self.htmlText = htmlText

    def parseHTML(self):
        soup = BeautifulSoup(self.htmlText, 'html.parser')
        self.title = soup.find('title').get_text()
        self.content = soup.find('div', {'class': 'content'}).get_text()
        self.footer = soup.find('div', {'class': 'footer'}).get_text()
        self.links = [link['href'] for link in soup.find_all('a')]
        return (self.title, self.content, self.footer, self.links)

    def clear(self):
        self.htmlText = ''
        self.parsing = ''
        self.lastTag = []
        self.title = ''
        self.content = ''
        self.footer = ''
        self.links = []

if __name__=='__main__':
    fileNames = ['1.html', '2.html', '3.html', '4.html', '5.html']
    if (len(sys.argv)>1):
        fileNames = sys.argv[1:]

    parser = HTML_Article_Parser()
    
    for fileName in fileNames:
        parser.fromFile(fileName)
        ret = parser.parseHTML()
        print(fileName + ': ')
        print("TITLE: ", ret[0])
        print("CONTENT: ", ret[1])
        print("FOOTER: ", ret[2])
        print("LINKS: ", ret[3])
