import itertools

words = ['tree', 'garden', 'olive']
assoc = [['branch', 'leaves', 'squirrel'],['branch', 'gnome', 'vegetation'],['martini', 'branch', 'sodium']]

print('----')
match = []
for i in range(0, len(words)-1):
    for j in range(i+1, len(words)):
        print(words[i] + ':',assoc[i])
        print(words[j] + ':', assoc[j])
        print('----')
        m = []
        for k in assoc[i]:
            for l in assoc[j]:
                if (k == l):
                    m.append(k)
        match.append(m)

print('----------------------------')
print(match)