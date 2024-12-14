# 귤 k개 골라 하나에 판매
# 서로 다른 종류의 수를 최소화
# k가 주어지면 최소한으로 종류를 count해서 result하기
from collections import Counter
def solution(k, tangerine):
    count = Counter(tangerine) # 귤 크기별 개수 세기
    sort_count = sorted(count.values(), reverse=True) # 내림차순으로 정렬

    answer = 0
    total = 0
    
    for num in sort_count:
        total += num
        answer += 1
        if total >= k:
            break
        
    return answer