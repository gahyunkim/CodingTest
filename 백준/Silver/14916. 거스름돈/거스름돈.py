import sys
input = sys.stdin.readline

# 거스름돈 액수 
n = int(input())

# 거스름돈 동전의 최소 개수
cnt = 0

# 가능한 5원으로 나누고, 나머지 부분을 처리
while n >= 0:
    if n % 5 == 0:            
        cnt += n // 5       
        print(cnt)          
        break
    n -= 2                   
    cnt += 1
else:
    print(-1)     