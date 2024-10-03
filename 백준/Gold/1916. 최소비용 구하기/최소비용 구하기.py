import heapq
import sys
input = sys.stdin.readline

N = int(input())
bus = int(input())

graph = [[] for _ in range(N + 1)]
road = []
for i in range(bus):
    a, b, cost = map(int, input().split())
    road.append((a, b, cost))

for a, b, cost in road:
    graph[a].append((b, cost))

start, end = map(int, input().split())
distances = [float("inf")] * (N + 1)
distances[start] = 0
heap = []
heapq.heappush(heap, (0, start))

while heap:
    dist, node = heapq.heappop(heap)
    # 현재 거리보다 더 큰 거리가 나오면 무시
    if dist > distances[node]:
        continue

    for next_node, next_dist in graph[node]:
        cost = dist + next_dist
        if cost < distances[next_node]:
            distances[next_node] = cost
            heapq.heappush(heap, (cost, next_node))
print(distances[end])