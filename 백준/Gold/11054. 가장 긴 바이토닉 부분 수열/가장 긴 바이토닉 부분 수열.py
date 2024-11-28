def longest_bitonic_subsequence(arr):
    n = len(arr)

    # 증가 부분 수열 (LIS)
    increase = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                increase[i] = max(increase[i], increase[j] + 1)

    # 감소 부분 수열 (LDS)
    decrease = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                decrease[i] = max(decrease[i], decrease[j] + 1)

    # 바이토닉 수열 최대 길이 계산
    max_length = 0
    for i in range(n):
        max_length = max(max_length, increase[i] + decrease[i] - 1)

    return max_length


# 입력 처리
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(longest_bitonic_subsequence(arr))
