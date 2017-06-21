quota = int(input())
months = int(input())
remaining = quota

for x in range(months):
    remaining -= int(input())
    remaining += quota

print(remaining)
