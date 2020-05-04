import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import itertools 
load_dotenv()

key =  os.getenv('PROJECT_API_KEY')
def getAssociatedWords(word):
    res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    res = res.json()
    res = res['response'][0]['items']
    return res
    
def solve(dictionary):
    def findGroupings(words):
        groupings = []
        for i in range(1, len(words)):
            groupings.extend(list(itertools.combinations(words, i+1)))
        pprint(groupings)
        return groupings

    def initiateSolve(dictionary):
        solution = {}
        words = []
        for i in dictionary:
            words.append(i)
        print(words)
        groupings = findGroupings(words)
        for g in groupings:
            matches = []
            for i in range(0, len(g)-1):
                a = dictionary[g[i]]
                for j in range(i+1, len(g)):
                    b = dictionary[g[j]]
                    similiar = []
                    for c in a:
                        for d in b:
                            if c["item"] == d["item"]:
                                e = {
                                    "item": c["item"],
                                    "weight1": c["weight"],
                                    "weight2": d["weight"],
                                }
                                similiar.append(e)
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
                        true.append(i)
            k = ""
            for i in g:
                k += i + " "
            solution[k] = true
        return solution
    solution = initiateSolve(dictionary)
    return solution
