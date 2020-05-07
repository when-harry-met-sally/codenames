import sys
from solver import solve, getAssociatedWords
from pprint import pprint
import time

# dictionary = {
#     ("apple",): ('cider', 'autumn'),
#     ("fall",): ('leaves', 'autumn','halloween', 'branch'),
#     ("pumpkin",): ('branch', "fall"),
#     # ("tree",): ('branch', 'chicken'),
#     # ("pineapple",): ('branch',),
#     # ("crack",): ('',)
# }

def handleArgs():
    dictionary = {}
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if i != 0:
            dictionary[tuple([arg])] = tuple(getAssociatedWords(arg))
    return dictionary

dictionary = handleArgs()

start = time.time()
solution = solve(dictionary)
end = time.time()
duration = end-start
print('---------------------')
pprint(solution)
print('---------------------')
print('time:', duration)
print('groupings:', len(solution))

