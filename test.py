import sys
from solver import solve, getAssociatedWords
from pprint import pprint
import time

# dictionary = {
#     # "tree": [{"item": 'branch'}, {"item": 'leaves'}, {"item": 'squirrel'}],
#     # "garden": [{"item": 'branch'}, {"item": 'gnome'}, {"item": 'fruit'}],
#     # "olive": [{"item": 'martini'}, {"item": 'branch'}, {"item": 'fruit'}],
#     ("apple",): ('cider', 'fall', "branch"),
#     ("fall",): ('eaves', 'fall','halloween', 'branch'),
#     ("pumpkin",): ('branch', "fall"),
#     ("tree",): ('branch',),
#     ("pineapple",): ('branch',),
#     ("crack",): ('',)
# }

import sys
from solver import solve, getAssociatedWords
from pprint import pprint
def handleArgs():
    dictionary = {}
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if i != 0:
            dictionary[tuple([arg])] = tuple(getAssociatedWords(arg))
    return dictionary

dictionary = handleArgs()
# pprint(dictionary)
# print('-----')
start = time.time()
solution = solve(dictionary)
print(len(solution))
end = time.time()

print(end-start)
# print('--------------SOLUTION--------------')
# pprint(solution)
