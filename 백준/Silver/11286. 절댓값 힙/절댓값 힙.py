import heapq as hq
import sys
input = sys.stdin.readline #입력을 100,000번 받기 때문에 효율위해
N = int(input())
pq = []
for _ in range(N):
    x = int(input()) 
    if x:
        hq.heappush(pq, (abs(x), x)) #절댓값과 원본값 같이 출력, 계산 용이
    else:
        print(hq.heappop(pq)[1] if pq else 0) #비어있으면 0 아니면?