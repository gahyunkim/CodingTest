def solve_wave_sequence():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    cases = list(map(int, data[1:]))
    
    # 최대 n 값 구하기
    max_n = max(cases)
    
    # DP 테이블 초기화
    dp = [0] * (max_n + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    if max_n >= 4:
        dp[4], dp[5] = 2, 2
    
    # 점화식으로 DP 값 채우기
    for i in range(6, max_n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    
    # 테스트 케이스 결과 출력
    results = [dp[n] for n in cases]
    print("\n".join(map(str, results)))

# 실행
solve_wave_sequence()