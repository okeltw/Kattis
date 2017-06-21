'''
Problem ID: bijele

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''

Final = [1, 1, 2, 2, 2, 8]
Current = [int(x) for x in input().split()]
Difference = [FinalItem - CurrentItem for FinalItem, CurrentItem in zip(Final, Current)]

output = ""
for item in Difference:
    output += str(item) + " "

print(output[:-1]) 

