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

if __name__ == '__main__':
    api = falcon.API()
    api.add_route('/search/{sentence}', SearchResource())
    httpd = simple_server.make_server('localhost', 8000, api)
    httpd.serve_forever()