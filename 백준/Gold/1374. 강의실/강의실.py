import sys
import heapq

input = sys.stdin.readline

# 강의 수 입력
N = int(input())

# 강의 정보 입력 및 시작 시간 기준 정렬
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[1])  # 시작 시간을 기준으로 정렬

# 최소 힙 생성
min_heap = []
max_rooms = 0

# 강의 순회
for lecture in lectures:
    start_time = lecture[1]
    end_time = lecture[2]

    while min_heap and min_heap[0] <= start_time:
        heapq.heappop(min_heap)
    
    heapq.heappush(min_heap, end_time)
    
    max_rooms = max(max_rooms, len(min_heap))

# 결과 출력
print(max_rooms)