import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import itertools 
from pprint import pprint
load_dotenv()

key =  os.getenv('PROJECT_API_KEY')
def getAssociatedWords(word):
    res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    res = res.json()
    res = res['response'][0]['items']
    return res

def solve(dictionary):
    solution = [i for i in dictionary]
    for i in range(0, len(solution)-1):
        for j in range(i+1, len(solution)):
            a = solution[i]
            b = solution[j]
            joined = tuple(set(a+b))
            matches = []
            for k in dictionary[a]:
                for l in dictionary[b]:
                    if k['item'] == l['item']:
                        matches.append(k)
            solution.append(joined)
            dictionary[joined] = tuple(matches)
    # pprint(dictionary)
    return dictionary

