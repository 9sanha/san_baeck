# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 입력의 마지막에는 0 두 개가 들어온다.
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다


def limite_sum(n1,n2,limite_num):
    if(n1==n2 and n1==0):
        print('프로그램을 종료하겠습니다')
        return 0
    elif (n1>limite_num or n2>limite_num or n1<1 or n2 <1):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
        return 1
    else:
        print(n1+n2)
        return 1

key=1
while(key==1):
    a,b = input('두 수를 입력하세요: ').split()
    a,b = int(a),int(b)
    key=limite_sum(a,b,9)
