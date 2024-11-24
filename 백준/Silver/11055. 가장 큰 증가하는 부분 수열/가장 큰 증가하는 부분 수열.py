n = int(input())  # 수열의 길이
arr = list(map(int, input().split()))  # 수열

# DP 배열 초기화
dp = arr[:]  # 각 위치에서 시작하는 증가 부분 수열의 합

# DP 계산
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:  # 증가 조건
            dp[i] = max(dp[i], dp[j] + arr[i])

# 결과 출력
print(max(dp))