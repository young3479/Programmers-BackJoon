A = input().split()
B = input()
count = 0

for item in A:
    if item == B:
        continue
    if item.startswith(B):
        count += 1

print(count)