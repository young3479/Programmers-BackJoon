import sys
input = sys.stdin.readline

n, c = map(int, input().split())
second = list(map(int, input().split()))

def race():
	count = 1
	for i in range(n):
		if i == n-1:
			continue
		if second[i+1] - second[i] <= c and second[i+1] - second[i] > 0:
			count += 1
		elif second[i+1] - second[i] > c:
			count = 1
			continue
		elif second[i+1] - second[i] <= 0:
			continue
	return count

print(race())
