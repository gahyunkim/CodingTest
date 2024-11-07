n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
s = int(input())
gom = list(map(int, input().split()))
visited = [False for _ in range(n + 1)]

for g in gom:
    visited[g] = True

def dfs(v):
    stack = [v]
    while stack:
        node = stack.pop()
        if visited[node]:
            return 'Yes'
        visited[node] = True
        if not graph[node]:
            return 'yes'
        for i in graph[node]:
            if not visited[i]:
                stack.append(i)
    return 'Yes'

print(dfs(1))
