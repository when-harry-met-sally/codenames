import itertools

dictionary = {
    "tree": ['branch', 'leaves', 'squirrel'],
    "garden": ['branch', 'gnome', 'vegetation'],
    "olive": ['martini', 'branch', 'sodium'],
    "apple": ['cider', '', 'newton'],
    "autumn": ['leaves', 'fall', 'season', 'halloween'],
    "pumpkin": ['halloween', 'branch']
}

def findGroupings(words):
    groupings = []
    for i in range(1, len(words)):
        groupings.extend(list(itertools.combinations(words, i+1)))
    return groupings

words = []
for i in dictionary:
    words.append(i)

groupings = findGroupings(words)
for g in groupings:
    matches = []
    for i in range(0, len(g)-1):
        for j in range(i+1, len(g)):
            a = dictionary[g[i]]
            b = dictionary[g[j]]
            # print(a)
            # print(b)
            m = []
            for c in a:
                for d in b:
                    # print(c, '-', d)
                    if c == d and c not in m:
                        m.append(c)
            # print('matches-', m)
            matches.append(m)
    if [] not in matches:
        print('---------------------------------------------')
        print(g)
        print(matches)
        print('---------------------------------------------')

key =  os.getenv('PROJECT_API_KEY')

def getAssociatedWords(word):
    res = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + key +'&text=' + word + '&lang=en&limit=300')
    return res.json()

test = getAssociatedWords("tree")
print(test)
