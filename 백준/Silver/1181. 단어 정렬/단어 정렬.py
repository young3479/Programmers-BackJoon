n = int(input())

words = []
for i in range(n):
    a = input()
    words.append(a)
words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)