import sys
from solver import solve, getAssociatedWords
from pprint import pprint
def handleArgs():
    dictionary = {}
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if i != 0:
            dictionary[arg] = getAssociatedWords(arg)
    return dictionary

dictionary = handleArgs()
print(dictionary)
print('-------')
solution = solve(dictionary)
pprint(solution)
