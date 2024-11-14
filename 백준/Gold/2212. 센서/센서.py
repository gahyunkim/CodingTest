import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
sensors = list(map(int, data[2:]))

sensors.sort()

distances = []
for i in range(1, N):
    distances.append(sensors[i] - sensors[i - 1])

distances.sort(reverse=True)

min_length = sum(distances[K - 1:])

print(min_length)