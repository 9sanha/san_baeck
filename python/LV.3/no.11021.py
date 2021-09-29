# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
def sum(a,b):
    return a+b
def limite(n,limite_num):
    if (n>limite_num or n<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
        print('프로그램을 종료합니다.')
        exit(0)
    else:
        return True

test_case = int(input('테스트 케이스 입력:'))
arr=[]
for i in range(0,test_case):
    print(i+1,' :',end=' ')
    a,b=input().split()
    if(limite(int(a),9) and limite(int(b),9)):
        arr.append(sum(int(a),int(b)))

print('--결과--')
count=1
for j in arr:
    print('Case #',count,': ',j)
    count+=1
