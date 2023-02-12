import requests
import json

host='http://localhost:8000'

endpoint = host + ''

def search(sentence):
    url = '{}/search/{}'.format(endpoint, sentence)
    url = url.replace(' ', '%20')
    print(url)
    res = requests.get(url)
    print(res.content)
    return res.json()

def test_search_single_word():
    data = search('ses')
    assert set(['1.html', '4.html']) == set(data['data'])

def test_search_sentence():
    data = search("un plombier maitrise l'eau")
    assert set(['1.html', "2.html", "5.html", "4.html"]) == set(data['data'])

def test_search_nonsense():
    data = search('dlmdmdl')
    assert [] == data['data']