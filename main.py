import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

key =  os.getenv('PROJECT_API_KEY')

def getAssociatedWords(word):
    res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    return res.json()

words = ['helicopter', 'board']
associated = []
for word in words:
    data = getAssociatedWords(word)
    items = data['response'][0]['items']
    associated.append(items)

best = []

for i in associated:
    for j in associated:
        if i != j:
            for k in i:
                for l in j:
                    if k['item'] == l['item']:
                        print(k)
                        print(l)
                        print(k['weight'] + l['weight'])
                        print('-')
                        if k['weight'] > 20 and l['weight'] > 20:
                            if k['item'].lower() not in words:
                                best.append({'word': k['item'], 'weight': k['weight'] + l['weight']})

print('----Best Results----')
for b in best:
    pprint(b)
