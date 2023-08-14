import heapq as hq
import sys
input = sys.stdin.readline # 입력을 100,000번 받기 때문에 효율을 위해
N = int(input())
min_heap = [] # 양수 보관
max_heap = [] # 음수 보관 -> 두 개 비교해서 값이 절대값이 더 작은 쪽 고르기(같다면 음수쪽 선택)
for _ in range(N):
    x = int(input()) 
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap)) 
            else:
                print(0)
