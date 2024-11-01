import sys
from collections import deque

input = sys.stdin.readline

# 정점의 수 n, 간선의 수 m, 시작 정점 r 입력
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 그래프이므로 반대 방향도 추가

# 방문 순서를 기록하기 위한 리스트
visited = [0] * (n + 1)
cnt = 1  # 방문 순서 기록용

# BFS 함수
def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = cnt  # 시작 정점 방문 표시
    cnt += 1

    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
            if not visited[i]:
                visited[i] = cnt
                cnt += 1
                queue.append(i)

# BFS 탐색 실행
bfs(graph, r, visited)

# 결과 출력
for i in range(1, n + 1):  # 1부터 n까지의 방문 순서 출력
    print(visited[i])
