import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  # 단방향 간선 추가

# 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 시작하는 도시의 거리는 0으로 설정

# BFS 탐색
queue = deque([x])
while queue:
    current = queue.popleft()
    
    for i in graph[current]:
        if distance[i] == -1:  # 방문하지 않은 도시라면
            distance[i] = distance[current] + 1
            queue.append(i)

# 거리 k인 도시 출력
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

# 거리가 k인 도시가 없는 경우
if not found:
    print(-1)
