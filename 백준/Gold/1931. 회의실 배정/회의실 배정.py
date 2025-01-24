n = int(input())

total = []

for i in range(n):
    a, b = map(int, input().split())
    total.append((a, b))

total.sort(key=lambda x: (x[1], x[0]))

count = 1
end = total[0][1]
for i in range(1, n):
    if total[i][0] >= end:
        end = total[i][1]
        count += 1

print(count)