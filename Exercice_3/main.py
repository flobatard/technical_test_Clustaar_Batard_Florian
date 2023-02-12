import reverse_index
import article_parser
import sys


#Take the html list and return {nameOfHtml}.json associated + reverse_index.json 
if __name__ == '__main__':
    fileNames = ['1.html', '2.html', '3.html', '4.html', '5.html']
    if (len(sys.argv)>1):
        fileNames = sys.argv[1:]
    
    articles = []

    for fileName in fileNames:
        article = article_parser.HTML_Article_Parser()
        article.fromFile(fileName)
        article.parseHTML()

        #Remove the extension and replace it with .json
        article.to_json('{}.json'.format('.'.join(fileName.split('.')[:-1])))

        articles.append(article)
    
    reverseIndex = reverse_index.ReverseIndex('words.txt')
    reverseIndex.feedMultiple(articles)
    reverseIndex.to_json('reverse_index.json')
