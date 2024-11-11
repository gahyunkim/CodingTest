import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    num = int(input())
    card = list(map(str, input().strip().split()))
    word = deque([card[0]])

    for i in card[1:]:
        if i > word[0]:
            word.append(i)
        else:
            word.appendleft(i)
    print(*word, sep="")