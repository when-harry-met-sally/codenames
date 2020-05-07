import sys
from solver import solve, getAssociatedWords
from pprint import pprint

dictionary = {
    # "tree": [{"item": 'branch'}, {"item": 'leaves'}, {"item": 'squirrel'}],
    # "garden": [{"item": 'branch'}, {"item": 'gnome'}, {"item": 'fruit'}],
    # "olive": [{"item": 'martini'}, {"item": 'branch'}, {"item": 'fruit'}],
    ("apple",): ('cider', 'fall', "branch"),
    ("fall",): ('eaves', 'fall','halloween', 'branch'),
    ("pumpkin",): ('branch', "fall"),
    ("tree",): ('branch',),
    ("pineapple",): ('branch',),
    ("crack",): ('branch',)
}
# dictionary = {
#     "tree": getAssociatedWords("tree"),
#     "garden": getAssociatedWords("garden"),
#     "olive": getAssociatedWords("olive")
# } 

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

# dictionary = handleArgs()
solution = solve(dictionary)
# print('--------------SOLUTION--------------')
# pprint(solution)
