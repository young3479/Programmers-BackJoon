#DFS 출력 - 스택
#BFS 출력 - 큐

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

# 그래프 구축 (한 번만)
for a, b in road:
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 인접 리스트를 오름차순으로 정렬
for adj in graph:
    adj.sort()

def dfs():
    visited = [False] * (N + 1)
    answer = []
    stack = []
    stack.append(V)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            answer.append(node)
            for i in reversed(graph[node]):#역순으로 추가하여 작은 번호부터 방문
                if not visited[i]:
                    stack.append(i)
    return answer



def bfs():
    visited = [False] * (N + 1)
    answer = []
    queue = deque()
    visited[V] = True
    answer.append(V)
    queue.append(V)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                answer.append(i)
                queue.append(i)
    return answer

print(' '.join(map(str, dfs())))
print(' '.join(map(str, bfs())))