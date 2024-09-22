def dfs(graph, visited, node):
    visited[node] = True
    count = 0
    for next in graph[node]:
        if not visited[next]:
            count += 1 + dfs(graph, visited, next)
    return count

# 입력 받기
n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]  # 1-based indexing을 위해 크기를 n+1로 설정
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터를 통해 감염된 컴퓨터 수 계산
print(dfs(graph, visited, 1))