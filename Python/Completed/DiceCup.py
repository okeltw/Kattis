'''
Problem ID: dicecup

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''

import operator

M, N = str(input()).split()

prob = {}
for m in range(1,int(M)+1):
    for n in range(1, int(N)+1):
        Sum = m+n
        if Sum in prob:
            prob[Sum] += 1
        else:
            prob[Sum] = 1

HighestProbs = [key for key, value in prob.items() if value == max(prob.values())]
for item in HighestProbs:
    print(item)

#print(max(prob, key=prob.get))
#max(iterprob.iteritems(), key=operator.itemgetter(1))[0]
 
