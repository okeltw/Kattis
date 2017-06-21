"""
Problem ID: reversebinary

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
"""

Num = int(input())
BinNum = bin(Num)[2:]
ReverseBinNum = BinNum[::-1]
ReverseNum = int(ReverseBinNum, 2)
print(ReverseNum)

