from collections import deque

# 나이트가 이동할 수 있는 8가지 방향 정의
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# BFS 함수
def bfs(start_x, start_y, target_x, target_y, board_size):
    # 방문 여부를 저장하는 배열
    visited = [[False] * board_size for _ in range(board_size)]
    queue = deque([(start_x, start_y, 0)])  # (현재 x, y, 이동 횟수)
    visited[start_x][start_y] = True

    while queue:
        x, y, moves_count = queue.popleft()

        # 목표 지점에 도달한 경우
        if x == target_x and y == target_y:
            return moves_count

        # 나이트의 모든 이동 방향 탐색
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < board_size and 0 <= ny < board_size and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves_count + 1))
    
    return -1  # 도달할 수 없는 경우 (문제에서는 항상 도달 가능하므로 필요 없음)

# 입력 처리
t = int(input())  # 테스트 케이스의 수
for _ in range(t):
    n = int(input())  # 체스판의 크기
    start_x, start_y = map(int, input().split())  # 시작 위치
    target_x, target_y = map(int, input().split())  # 목표 위치
    
    if start_x == target_x and start_y == target_y:
        print(0)  # 시작점과 목표점이 같은 경우
    else:
        print(bfs(start_x, start_y, target_x, target_y, n))
