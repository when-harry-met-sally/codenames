import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import itertools 
from pprint import pprint
load_dotenv()

key =  os.getenv('PROJECT_API_KEY') #SORT THAAT WLL FIX SOME BUGS
def convertToJSON(dictionary):
    friendly = []
    pprint('--converting to json friendly object--')
    for item in list(dictionary.items()):
        solution = {
            "words": list(item[0]),
            "solutions": list(item[1])
        }
        friendly.append(solution)
    return friendly

def getAssociatedWords(word):
    # res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    res = requests.get('https://api.datamuse.com/words?ml=' + word + '&max=100')
    res = res.json()
    print(res)
    return res

def solve(dictionary):
    solution = [i for i in dictionary]
    for i in range(0, len(solution)-1):
        for j in range(i+1, len(solution)):
            a = solution[i]
            b = solution[j]
            joined = tuple(sorted(list(set(a+b)), key=len))
            matches = []
            for k in dictionary[a]:
                for l in dictionary[b]:
                    if k['word'] == l['word'] and not itemInArray(matches, k['word']):
                        matches.append(k)
            solution.append(joined)
            dictionary[joined] = tuple(matches)

    return convertToJSON(dictionary)

def itemInArray(array, item):
    for a in array:
        if a['word'] == item:
            return True
    return False