import sys
from bisect import bisect_left

def longest_increasing_subsequence(arr):
    lis = []
    for num in arr:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

# 입력 처리
input = sys.stdin.read
data = input().split()

n = int(data[0])
sequence = list(map(int, data[1:]))

# LIS 계산
lis_length = longest_increasing_subsequence(sequence)

# 최소 이동 횟수 계산 및 출력
print(n - lis_length)
