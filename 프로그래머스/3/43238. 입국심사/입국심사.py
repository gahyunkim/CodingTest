def solution(n, times):
    # 시작 시간과 끝 시간을 설정
    start = 1
    end = max(times) * n
    
    answer = end  # 최악의 경우 시간을 초기 답안으로 설정해둠
    
    while start <= end:
        mid = (start + end) // 2  # 현재 예상 최소 시간
        people_checked = sum(mid // time for time in times)  # mid 시간 동안 심사할 수 있는 총 인원 수
        
        if people_checked >= n:
            # 충분한 인원을 처리할 수 있으면 시간을 줄여서 더 최적의 값을 찾음
            answer = mid
            end = mid - 1
        else:
            # 인원을 처리할 수 없다면 시간을 늘려야 함
            start = mid + 1
    
    return answer
