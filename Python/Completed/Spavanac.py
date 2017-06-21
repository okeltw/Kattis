'''
Problem ID: spavanac

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.3
'''

Hours, Minutes = str(input()).split()
Hours = int(Hours)
Minutes = int(Minutes)

Minutes -= 45
if Minutes < 0:
    Minutes += 60 
    Hours -= 1
    if Hours < 0:
        Hours += 24

print(Hours, Minutes)
