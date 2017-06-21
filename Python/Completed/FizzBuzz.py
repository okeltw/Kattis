'''
Problem ID: fizzbuzz

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''

X, Y, N = str(input()).split()
X = int(X)
Y = int(Y)

for i in range(1, int(N)+1):
    if i%X == 0 and i%Y == 0:
        print('FizzBuzz')
    elif i%X == 0:
        print('Fizz')
    elif i%Y == 0:
        print('Buzz')
    else:
        print(i)
