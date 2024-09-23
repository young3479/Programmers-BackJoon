def dfs_stack(graph, visited, start_node):
    stack = [start_node]
    visited[start_node] = True
    count = 0
    while stack:
        node = stack.pop()
        for next in graph[node]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True
                count += 1
    return count
    
n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ] #1부터 인덱싱하기 위해 n+1로 설정
visited = [False] * (n+1) #1부터 인덱싱하기 위해 n+1로 설정

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs_stack(graph, visited, 1))