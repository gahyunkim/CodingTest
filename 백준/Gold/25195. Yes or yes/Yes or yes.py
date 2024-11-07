from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
s = int(input())
gom = list(map(int, input().split()))
visited = [False for _ in range(n+1)]

def bfs():
    q = deque()
    q.append(1)
    if visited[1]:
        return 'Yes'
    visited[1] = True
    while q:
        v = q.popleft()
        if not graph[v]:
            return 'yes'
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return 'Yes'
    
for g in gom:
    visited[g] = True
print(bfs())