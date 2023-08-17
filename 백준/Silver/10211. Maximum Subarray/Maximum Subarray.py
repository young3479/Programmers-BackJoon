import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    
    prefix_sum = [0] * (n + 1)
    for j in range(n):
        prefix_sum[j + 1] = prefix_sum[j] + x[j]
    
    max_sum = x[0]
    min_sum = 0
    
    for j in range(1, n + 1):
        max_sum = max(max_sum, prefix_sum[j] - min_sum)
        min_sum = min(min_sum, prefix_sum[j])
        
    print(max_sum)
