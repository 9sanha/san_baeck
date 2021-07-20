# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

def limite(n,limite_num):
    if (n>limite_num or n<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
    else:
        return True

n = int(input('숫자 입력: '))
star=''
if(limite(n,100)):
    bl=n-1
    for i in range(1,n+1):
        star = ' '*bl
        for j in range(0,i):
            star+='*'
        print(star)
        bl-=1