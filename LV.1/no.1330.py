# 문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
# 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
#
# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# 제한
# -10,000 ≤ A, B ≤ 10,000

def limite(a,b):
    if (a>10000 or a<-10000 or b>10000 or b<-10000):
        print('입력오류 : 입력한 수가 입력 범위를 벗어났습니다.')
    else:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('==')

a,b =input('두 수를 입력하시오 (예시:2 5): ').split()
limite(int(a),int(b))

