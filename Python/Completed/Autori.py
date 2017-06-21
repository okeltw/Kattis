'''
Problem ID: autori

CPU Time limit: 1 second

Memory limit: 1024 MB

Difficulty: 1.2
'''
Names = str(input()).split("-")
Acronym = ""

for name in Names:
    Acronym += name[0]

print(Acronym)
