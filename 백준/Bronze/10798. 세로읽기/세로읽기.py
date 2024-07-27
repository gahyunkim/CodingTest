lines= []
length = [] # 입력받는 단어 각각의 길이를 나타내는 length 
ans = ''
for _ in range(5):
    line=input()
    length.append(len(line))
    lines.append(line)



for j in range(max(length)):
    for i in range(5):
    # if문에서 j가 length[i], 즉 index 범위를 벗어난다면 글자 추가가 일어나지 않는다 ! 
        if j< length[i]:
            ans+=lines[i][j]

print(ans)