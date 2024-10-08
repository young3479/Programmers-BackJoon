N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

max_health_loss = 100
dp = [0] * max_health_loss

for i in range(N):
    for health_lost in range(max_health_loss - 1, L[i] - 1, -1):
        dp[health_lost] = max(dp[health_lost], dp[health_lost - L[i]] + J[i])

print(max(dp))
