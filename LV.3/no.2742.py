# 문제
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
def limite(n,limite_num):
    if (n>limite_num or n<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
    else:
        return True

n = int(input('자연수를 입력하세요: '))

if(limite(n,100000)):
    for i in range(0,n):
        print(n-i)

