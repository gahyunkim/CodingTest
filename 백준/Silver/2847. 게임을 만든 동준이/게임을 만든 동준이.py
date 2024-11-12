n = int(input())
level = []

for i in range(n):
    level.append(int(input()))

cnt = 0
for i in range(n-2, -1, -1):
    if level[i] >= level[i+1]:
        cnt += level[i] - level[i+1] + 1
        level[i] = level[i+1]-1

print(cnt)