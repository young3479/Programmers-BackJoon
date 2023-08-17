import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

preSum = 0
preArr = [0]

M = int(input())

for i in A:
  preSum += i
  preArr.append(preSum)

for _ in range(M):
  i, j = map(int, input().split())
  print(preArr[j] - preArr[i - 1])
