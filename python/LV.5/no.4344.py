# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

def percnt(score):
    sum = 0 #평균 구할때 씀
    N = score[0]
    for i in range(N):
        sum+=score[i+1]
    avr = sum/score[0]
    sum = 0 # 평균 넘는 학생들 카운트용
    for i in range(N):
        if score[i+1] >avr:
            sum+=1
    return sum/N*100

test_case = int(input('test case: '))

percent = []

for i in range(test_case):
    N_score = []
    print(i+1,':',end='')
    N_score = map(int,input().split())
    N_score = list(N_score)
    percent.append(percnt(N_score))

for i in range(test_case):
    print(round(percent[i],3),'%') # round는 소숫점 조정할 때 씀