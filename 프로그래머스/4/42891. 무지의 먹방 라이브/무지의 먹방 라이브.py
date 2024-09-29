import heapq

def solution(food_times, k):
    # 모든 음식 섭취 시간이 0인 경우, 중단된 이후에는 더 섭취할 음식이 없으므로 -1 반환
    if sum(food_times) <= k:
        return -1
    
    # 우선순위 큐에 (음식의 시간, 음식 번호) 삽입
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))
    
    total = 0  # 전체 소요 시간
    pre_time = 0  # 이전에 다 먹은 음식의 시간
    length = len(food_times)  # 남아있는 음식의 개수
    
    # 우선순위 큐를 통해 음식을 먹음
    while total + ((hq[0][0] - pre_time) * length) <= k:
        curr_time, _ = heapq.heappop(hq)  # 현재 가장 적은 시간을 가진 음식
        total += (curr_time - pre_time) * length
        length -= 1  # 다 먹은 음식 제외
        pre_time = curr_time  # 이전 음식 시간 갱신
    
    # 남아있는 음식 중 몇 번째 음식부터 다시 먹어야 하는지 찾기
    remain_foods = sorted(hq, key=lambda x: x[1])  # 음식 번호 기준으로 정렬
    return remain_foods[(k - total) % length][1]