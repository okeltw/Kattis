'''
Problem ID: speedlimit

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.3
'''

NumPairs = int(input())

while NumPairs != -1:
    elapsed = 0
    distance = 0
    for p in range(NumPairs):
        speed, time = input().split()
        distance += int(speed) * (int(time) - elapsed)
        elapsed = int(time)

    print(distance, 'miles')

    NumPairs = int(input())

