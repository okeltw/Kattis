'''
Problem ID: oddities

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''

Num = int(input())

for n in range(Num):
    x = int(input())
    if x%2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')
