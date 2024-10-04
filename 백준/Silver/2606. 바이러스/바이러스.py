import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
network = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[1] = True
for a, b in network:
    graph[a].append(b)
    graph[b].append(a)


def dfs_stack():
    stack = []
    stack.append(1)
    count = 0

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                count += 1
    return count


print(dfs_stack())