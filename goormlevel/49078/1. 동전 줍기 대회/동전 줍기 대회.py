import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))

# DP 배열 초기화
dp = [0] * n

# 초기 조건 설정
dp[0] = coin[0]
max_sum = dp[0]

# DP 배열 채우기
for i in range(1, n):
    dp[i] = max(coin[i], dp[i - 1] + coin[i])
    max_sum = max(max_sum, dp[i])

print(max_sum)
