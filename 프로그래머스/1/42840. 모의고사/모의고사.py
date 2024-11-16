def solution(answers):
    dropout1 = [1, 2, 3, 4, 5]
    dropout2 = [2, 1, 2, 3, 2, 4, 2, 5]
    dropout3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    answer = []  # answer 리스트 초기화

    # 점수 계산
    for i in range(len(answers)):
        if answers[i] == dropout1[i % 5]:
            score[0] += 1
        if answers[i] == dropout2[i % 8]:
            score[1] += 1
        if answers[i] == dropout3[i % 10]:
            score[2] += 1

    # 최고 점수와 동일한 사람의 번호 추가
    for idx, num in enumerate(score):
        if num == max(score):
            answer.append(idx + 1)

    return answer
