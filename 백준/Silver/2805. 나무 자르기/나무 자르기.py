import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0  
end = max(trees)
mid = 0

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in trees:
        if i > mid:
            result += (i - mid)
    
    if result >= m:  
        start = mid + 1
    else:  
        end = mid - 1

print(end)