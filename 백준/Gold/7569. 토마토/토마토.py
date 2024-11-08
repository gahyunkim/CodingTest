from collections import deque

# 입력 받기
m, n, h = map(int, input().split())  # 가로, 세로, 높이
tomato_box = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    tomato_box.append(layer)

# 방향 벡터 정의 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

# BFS를 위한 큐 초기화
queue = deque()

# 익은 토마토의 위치를 큐에 추가하고, BFS 시작점으로 설정
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato_box[z][x][y] == 1:  # 익은 토마토
                queue.append((z, x, y))

# BFS 수행
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):  # 6방향 탐색
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            # 범위를 벗어나지 않는지, 그리고 익지 않은 토마토(0)인지 확인
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tomato_box[nz][nx][ny] == 0:
                tomato_box[nz][nx][ny] = tomato_box[z][x][y] + 1
                queue.append((nz, nx, ny))

bfs()  # BFS 시작

# 모든 토마토가 익었는지 확인 및 최대 일수 계산
max_days = 0
all_ripe = True

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato_box[z][x][y] == 0:  # 익지 않은 토마토가 남아 있는 경우
                all_ripe = False
            max_days = max(max_days, tomato_box[z][x][y])

# 결과 출력
if not all_ripe:
    print(-1)
else:
    print(max_days - 1)  # 첫 날이 1로 시작했으므로 -1 해서 일수 계산
