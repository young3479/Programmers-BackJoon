# 예산의 상한선을 구하는 것
N = int(input()) #지방의 수
req = list(map(int, input().split())) #예산 요청
M = int(input()) #총 예산

#이분 탐색 범위
lo = 0
hi = max(req) #지방 예산 요청 중에 가장 큰 값까지만 보면 됨
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M

while lo <= hi:
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid -1

    mid = (lo + hi) // 2
    
print(ans)

