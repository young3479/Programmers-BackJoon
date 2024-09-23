def dfs(graph, visited, node):
    visited[node] = True
    count = 0
    for next in graph[node]:
        if not visited[next]:
            count += 1 + dfs(graph, visited, next)
    return count
    
n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ] #1부터 인덱싱하기 위해 n+1로 설정
visited = [False] * (n+1) #1부터 인덱싱하기 위해 n+1로 설정

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, visited, 1))