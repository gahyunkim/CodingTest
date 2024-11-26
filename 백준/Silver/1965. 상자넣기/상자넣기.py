n = int(input())
boxes = list(map(int, input().split()))

# n개 만큼 dp 배열을 초기화해준다
dp = [1] * n

# DP로 LIS 계산
for i in range(n):
    for j in range(i):
        if boxes[j] < boxes[i]:  # 상자를 쌓을 수 있는 경우
            dp[i] = max(dp[i], dp[j] + 1)

# 정답 출력
print(max(dp))