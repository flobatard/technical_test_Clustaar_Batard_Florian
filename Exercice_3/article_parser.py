import html
import html.parser
import sys
import json

class HTML_Article_Parser(html.parser.HTMLParser):
    pageName = ''
    htmlText = ''
    parsing = ''
    lastTag = []
    title = ''
    content = ''
    footer = ''
    link = []
    parsed = False

    def handle_starttag(self, tag, attrs):
        self.lastTag.append(tag)
        if (tag == 'title'):
            self.parsing = 'title'
        elif (tag == 'div' and ('class', 'content') in attrs):
            self.parsing = 'content'
        elif (tag == 'div' and ('class', 'footer') in attrs):
            self.parsing = 'footer'
        elif (tag == 'a'):
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])
    
    def handle_endtag(self, tag):
        self.lastTag.pop()
        if (tag == 'title' and self.parsing == 'title'):
            self.parsing = ''
        elif (tag == 'div' and self.parsing == 'content'):
            self.parsing = ''
        elif (tag == 'div' and self.parsing == 'footer'):
            self.parsing = ''

    def handle_data(self, data):
        if (self.parsing == 'title'):
            self.title = self.title + data
        elif (self.parsing == 'content'):
            self.content = self.content + data
        elif (self.parsing == 'footer'):
            self.footer = self.footer + data
        

    def fromFile(self, fileName):
        self.clear()
        f = open(fileName, encoding='utf-8')
        self.pageName = fileName
        self.htmlText = f.read()
        f.close()

    def fromHtmlText(self, htmlText, pageName):
        self.clear()
        self.htmlText = htmlText
        self.pageName = pageName

    def parseHTML(self):
        if (not self.parsed):
            self.feed(self.htmlText)
            self.parsed = True
        return (self.title, self.content, self.footer, self.links)

    def to_json(self, fileName):
        f = open(fileName, encoding='utf-8', mode='w')
        obj = {'title' : self.title, 'content' : self.content, 'footer' : self.footer, 'links' : self.links}
        f.write(json.dumps(obj, indent=4))
        f.close()

    def clear(self):
        self.htmlText = ''
        self.parsing = ''
        self.lastTag = []
        self.title = ''
        self.content = ''
        self.footer = ''
        self.links = []
        self.parsed = False

if __name__=='__main__':
    fileNames = ['1.html', '2.html', '3.html', '4.html', '5.html']
    if (len(sys.argv)>1):
        fileNames = sys.argv[1:]

    parser = HTML_Article_Parser()
    
    for fileName in fileNames:
        parser._from_file(fileName)
        ret = parser.parseHTML()
        print(fileName + ': ')
        print("TITLE: ", ret[0])
        print("CONTENT: ", ret[1])
        print("FOOTER: ", ret[2])
        print("LINKS: ", ret[3])
