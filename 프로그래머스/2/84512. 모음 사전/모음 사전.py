from itertools import product

def solution(word):
    vowels = ['A','E','I','O','U']
    dict = []
    answer = 0
    
    for i in range(5):
        for j in product(vowels,repeat = i+1):
            dict.append(''.join(j))
    dict.sort()
    return dict.index(word)+1

    


