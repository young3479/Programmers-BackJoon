N = int(input())
D = dict()

for _ in range(N):
    book = input()
    if book in D:
        D[book] += 1
    else:
        D[book] = 1
m = max(D.values())
answer = []
for k, v in D.items():
    if v == m:
        answer.append(k)
answer.sort()
print(answer[0])