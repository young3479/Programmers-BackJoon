def dfs(computers, visited, node):
    visited[node] = True # 방문 처리
    for idx, connected in enumerate(computers[node]):
        if connected and not visited[idx]: # 연결되어 있고 방문 안했으면
            dfs(computers, visited, idx) # 방문

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    return answer