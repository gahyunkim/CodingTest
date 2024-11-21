N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

# 마주 보는 면의 인덱스 설정
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

max_sum = 0

# 첫 번째 주사위의 아랫면을 0~5까지 설정
for bottom in range(6):
    total = 0
    top = opposite[bottom]
    current_bottom_value = dices[0][bottom]
    current_top_value = dices[0][top]

    # 현재 주사위에서 옆면 중 최댓값 더하기
    total += max([dices[0][i] for i in range(6) if i != bottom and i != top])

    # 두 번째 주사위부터 처리
    for i in range(1, N):
        # 이전 주사위의 윗면 값이 다음 주사위의 아랫면 값
        bottom = dices[i].index(current_top_value)
        top = opposite[bottom]
        current_bottom_value = dices[i][bottom]
        current_top_value = dices[i][top]

        # 옆면 중 최댓값 계산
        total += max([dices[i][j] for j in range(6) if j != bottom and j != top])

    # 최댓값 갱신
    max_sum = max(max_sum, total)

print(max_sum)

