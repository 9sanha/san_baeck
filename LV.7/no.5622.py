#문제가 왜이랭,,

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input('단어 입력 하십쇼:')
total=0
for i in range(len(word)):
    time = 2
    for j in range(len(dial)):
        time+=1
        if word[i] in dial[j]: # 순서 바꿔서 쓰면 답이 없음..
            total+=time
            break
print(total)

