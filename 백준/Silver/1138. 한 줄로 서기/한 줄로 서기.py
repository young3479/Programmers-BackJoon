def line_up(N, info):
    # 줄을 서는 사람들의 순서를 담을 리스트 (초기값은 모두 빈 자리 -1로 설정)
    result = [-1] * N
    
    # 키가 작은 사람(1부터 N까지)부터 배치
    for i in range(N):
        count = info[i]  # 자신보다 키 큰 사람이 왼쪽에 몇 명 있는지
        for j in range(N):
            # 빈 자리가 있고, count가 0이면 그 자리에 i+1(키가 i+1인 사람)을 배치
            if result[j] == -1:
                if count == 0:
                    result[j] = i + 1
                    break
                else:
                    count -= 1
    
    # 결과 출력
    return result

# 입력 받기
N = int(input())  # 사람의 수
info = list(map(int, input().split()))  # 각 사람의 왼쪽에 있는 키 큰 사람의 수

# 결과 출력
print(*line_up(N, info))
