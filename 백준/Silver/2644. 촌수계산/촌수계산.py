n = int(input())
parent, child = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, end, visited, count):
    visited[start] = True
    if start == end:
        return count
    
    for i in graph[start]:
        if not visited[i]:
            result = dfs(graph, i, end, visited, count + 1)
            if result != -1:  # 경로를 찾은 경우
                return result
    return -1  # 경로를 찾지 못한 경우

visited = [False] * (n + 1)
result = dfs(graph, parent, child, visited, 0)

print(result)
