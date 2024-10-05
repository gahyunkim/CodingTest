n = int(input())
time = list(map(int,input().split()))

time.sort()

count = 0

for i in range(n):
    for j in range (0, i+1):
        count += time[j]
    
print(count)