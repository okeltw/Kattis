''' 
Problem ID: trik

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.3
'''

Moves = input()
Position = 1

Map = { 'A1': 2, 'A2': 1,
        'B2': 3, 'B3': 2,
        'C1': 3, 'C3': 1 }

for move in list(Moves):
    pattern = move + str(Position)
    if pattern in Map:    
        Position = Map[pattern]

print(Position)    
