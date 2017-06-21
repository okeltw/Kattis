'''
Problem ID: cold

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''
NumTemps = input()
Temps = str(input()).split()
NumBelowZero = 0

for Temp in Temps:
    if int(Temp) < 0:
        NumBelowZero += 1

print(NumBelowZero)
