N, M = map(int, input().split())
rice = list(map(int, input().split()))
start = 0
end = max(rice)
remain_rice = []

while start <= end: #이진탐색
    mid = (start+end) // 2
    total = 0
    for i in rice:
        if i > mid: 
            total += i - mid
    if total < M: 
        end = mid - 1
    else:
        result = mid #혹시 다음을 못돌 수 있으니 일단 저장
        start = mid + 1
print(result)