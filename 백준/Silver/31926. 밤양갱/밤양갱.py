import sys
input = sys.stdin.read

def min_time(n):
    count = 8  # 첫 번째 "daldidalgo" 생성 시간
    i = 1

    # n에 가장 가까운 2의 제곱수를 찾는 반복문
    while 2 ** i < n:
        i += 1
    
    # 필요한 복사 횟수와 마지막 "daldidan" 추가 시간 계산
    count += i + (2 if 2 ** i == n else 1)
    
    return count

# 입력 및 결과 출력
n = int(input().strip())
print(min_time(n))
