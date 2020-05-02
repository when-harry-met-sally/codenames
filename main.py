import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import sys
import itertools 
load_dotenv()

key =  os.getenv('PROJECT_API_KEY')
# dictionary = {
#     "tree": [{"item": 'branch'}, {"item": 'leaves'}, {"item": 'squirrel'}],
#     "garden": [{"item": 'branch'}, {"item": 'gnome'}, {"item": 'vegetation'}],
#     "olive": [{"item": 'martini'}, {"item": 'branch'}, {"item": 'sodium'}],
#     "apple": [{"item": 'cider'}, {"item": 'newton'}],
#     "autumn": [{"item": 'leaves'}, {"item": 'fall'}, {"item": 'season'}, {"item": 'halloween'}, {"item": 'branch'}],
#     "pumpkin": [{"item": 'halloween'}, {"item": 'branch'}]
# }

def getAssociatedWords(word):
    res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    res = res.json()
    res = res['response'][0]['items']
    return res

dictionary = {
    "tree": getAssociatedWords("tree"),
    "garden": getAssociatedWords("garden"),
    "olive": getAssociatedWords("olive")
}


def findGroupings(words):
    groupings = []
    for i in range(1, len(words)):
        groupings.extend(list(itertools.combinations(words, i+1)))
    return groupings

words = []
for i in dictionary:
    words.append(i)
print(words)
groupings = findGroupings(words)
for g in groupings:
    print('-----', g, '----')
    matches = []
    for i in range(0, len(g)-1):
        a = dictionary[g[i]]
        for j in range(i+1, len(g)):
            b = dictionary[g[j]]
            similiar = []
            for c in a:
                for d in b:
                    if c["item"] == d["item"]:
                        similiar.append(c)
            
            matches.append(similiar)
    true = []
    if len(matches) != 0:
        initial = matches[0]
        matches.pop(0)
        for i in initial:
            found = True
            for j in matches:
                if i not in j:
                    found = False
            if found == True:
                print(i)
    # print('---------------------------------------------')
    # print(g)
    # pprint(matches)
    # print('---------------------------------------------')

