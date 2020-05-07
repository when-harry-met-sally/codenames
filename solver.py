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

solution = {}
def solve(dictionary):
    test1 = solve2(dictionary)
    print('first iteration')
    pprint(test1)
    print('second iteration')
    test2 = solve2(test1)
    pprint(test2)
    

def solve2(dictionary):
    words = [i for i in dictionary]
    temp = {}
    for i in range(0, len(words)-1):
        a = words[i]
        for j in range(1, len(words)):
            b = words[j]
            if a != b:
                similiar = []
                joined = tuple(set(a+b))
                # print(joined)
                for c in dictionary[a]:
                    for d in dictionary[b]:
                        if c == d:
                            similiar.append(c)
                temp[joined] = similiar

    return temp
