import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수
numbers = list(map(int, input().split())) # 수열 입력

prefix_sum = [0] * (N + 1) # 누적 합을 저장할 배열 초기화
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

M = int(input()) # 구간의 개수
for _ in range(M):
    i, j = map(int, input().split()) # 구간의 시작과 끝
    print(prefix_sum[j] - prefix_sum[i - 1]) # 누적 합을 이용하여 구간의 합 출력
