from itertools import combinations
heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7):
    if sum(i) == 100:
        for heights in sorted(i):
            print(heights)
        break
    