graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

dice = list(map(int, input().split()))
answer = 0


def backtracking(depth, result, horses):
    global answer
    if depth == 10:  # 모든 주사위를 사용한 경우
        answer = max(answer, result)
        return

    for i in range(4):  # 4개의 말 중 하나를 선택
        current_position = horses[i]  # 현재 말의 위치

        # 갈 수 있는 경로 중 파란색 칸 처리
        if len(graph[current_position]) == 2:
            next_position = graph[current_position][1]  # 파란 화살표로 이동
        else:
            next_position = graph[current_position][0]  # 빨간 화살표로 이동

        # 주사위 값을 소진하면서 이동
        for _ in range(1, dice[depth]):
            if next_position == 32:  # 도착 지점에 도달한 경우
                break
            next_position = graph[next_position][0]

        # 말이 도착 지점이거나, 다른 말이 없는 경우
        if next_position == 32 or (next_position < 32 and next_position not in horses):
            # 말 위치 업데이트 및 백트래킹 호출
            previous_position = horses[i]
            horses[i] = next_position

            # 재귀 호출: 다음 주사위로 진행
            backtracking(depth + 1, result + score[next_position], horses)

            # 말 위치 원복 (백트래킹)
            horses[i] = previous_position


# 초기화 및 실행
backtracking(0, 0, [0, 0, 0, 0])
print(answer)
