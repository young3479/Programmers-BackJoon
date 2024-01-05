import heapq
def solution(N, rode, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in rode:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        dist = [float('inf')] * (N + 1)
        dist[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            d, node = heapq.heappop(queue)
            if dist[node] < d:
                continue
            for adj, w in graph[node]:
                new_dist = d + w
                if new_dist < dist[adj]:
                    dist[adj] = new_dist
                    heapq.heappush(queue, (new_dist, adj))

        return dist

    shortest_dist = dijkstra(1)
    return sum(1 for d in shortest_dist if d <= K)


