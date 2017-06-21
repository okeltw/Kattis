'''
Problem ID: pot

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''

NumAddends = int(input())
X = 0

for x in range(NumAddends):
    Addend = str(input())
    Base = Addend[:-1]
    Pow = Addend[-1:]
    X += int(Base) ** int(Pow)

print(X)
