import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import sys
import itertools 
load_dotenv()

key =  os.getenv('PROJECT_API_KEY')
dictionary = {
    "tree": ['branch', 'leaves', 'squirrel'],
    "garden": ['branch', 'gnome', 'vegetation'],
    "olive": ['martini', 'branch', 'sodium'],
    "apple": ['cider', 'newton'],
    "autumn": ['leaves', 'fall', 'season', 'halloween', 'branch'],
    "pumpkin": ['halloween', 'branch']
}
pprint(dictionary)
# def getAssociatedWords(word):
#     res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=50')
#     res = res.json()
#     res = res['response'][0]['items']
#     return res


def findGroupings(words):
    groupings = []
    for i in range(1, len(words)):
        groupings.extend(list(itertools.combinations(words, i+1)))
    return groupings

# tree = getAssociatedWords("tree")
# garden = getAssociatedWords("garden")
# apple = getAssociatedWords("apple")
# dictionary = {
#     "tree": tree,
#     "garden": garden,
#     "apple": apple
# }


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
                    if c == d:
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

