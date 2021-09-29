# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#
# 출력
# 1부터 n까지 합을 출력한다.

def limite(n):
    if (n>10000 or n<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~10,000)')
    else:
        return True
n=int(input('숫자를 입력하세요: '))

if(limite(n)):
    a=0
    for i in range(1,n+1):
        a+=i
    print(a)

