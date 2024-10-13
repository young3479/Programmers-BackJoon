import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distances = [float('inf')] * (N+1)
    distances[1] = 0 #출발 노드
    
    for a, b, cost in road: #가중치 양방향 그래프
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    heap = []
    heapq.heappush(heap, (0, 1)) #가중치가 0인 1번 노드 삽입
    
    while heap: #힙이 비어있기 전까지
        dist, node = heapq.heappop(heap) #가중치, 노드 꺼내기
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    
    #distances 배열이 K이하인 노드의 개수만 세기
    answer = 0
    for i in range(1, len(distances)):
        if distances[i] <= K:
            answer += 1
    return answer