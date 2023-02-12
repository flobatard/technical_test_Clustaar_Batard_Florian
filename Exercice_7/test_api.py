import urllib.request
import json

host='http://localhost:8000'

endpoint = host + ''

def search(sentence):
    url = '{}/search/{}'.format(endpoint, sentence)
    url = url.replace(' ', '%20')
    print(url)
    res = urllib.request.urlopen(url)
    data = res.read().decode()
    print(data)
    return json.loads(data)

def test_search_single_word():
    data = search('ses')
    assert set(['1.html', '4.html']) == set(data['data'])

def test_search_sentence():
    data = search("un plombier maitrise l'eau")
    assert set(['1.html', "2.html", "5.html", "4.html"]) == set(data['data'])

def test_search_nonsense():
    data = search('dlmdmdl')
    assert [] == data['data']