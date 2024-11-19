from itertools import permutations

def is_prime(number):
    if number < 2:  # 0과 1은 소수가 아님
        return False
    for i in range(2, int(number ** 0.5) + 1):  # 숫자의 제곱근까지 확인
        if number % i == 0:
            return False
    return True

def solution(numbers):
    possible_numbers = set()  # 중복 제거를 위한 set 사용
    
    # 문자열로부터 모든 순열 생성
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            possible_numbers.add(int("".join(perm)))  # 순열을 숫자로 변환하여 set에 추가

    # 소수 개수 세기
    prime_count = sum(1 for num in possible_numbers if is_prime(num))
    return prime_count
