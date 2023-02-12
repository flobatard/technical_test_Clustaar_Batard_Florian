import falcon
import json
import search
from wsgiref import simple_server


class SearchResource:
    def on_get(self, req, resp, sentence):
        words = sentence.split(' ')
        data = search.searchInReversedSentenceindexOR(words, 'reverse_index.json')
        ret = {'data' : list(data)}
        resp.body = json.dumps(ret)

class HelloResource:
    def on_get(self, req, resp):
        resp.body = "Hello, World!"


api = falcon.API()
api.add_route('/search/{sentence}', SearchResource())
api.add_route('/', HelloResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('localhost', 4242, api)
    httpd.serve_forever()