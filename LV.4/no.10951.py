# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
# 문제설명 매우 빈약한데 이 문제가 원하는건 반복문에서 예외처리를 할 수 있는가인듯
def limite_sum(n1,n2,limite_num):
    if (n1>limite_num or n2>limite_num or n1<1 or n2 <1):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
    else:
        print(n1+n2)

while True:
    try:
        a,b=map(int,input('두 수를 입력하세요:').split())
        limite_sum(a,b,9)
    except:
        print('입력오류: 프로그램을 종류합니다.')
        exit(0)
