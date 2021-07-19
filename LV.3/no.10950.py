# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
#설명이 맘에 안드네요ㅎ...
def sum(a,b):
    return a+b
test_case = int(input('테스트 케이스 입력:'))
arr=[]
for i in range(0,test_case):
    print(i+1,' :',end=' ')
    a,b=input().split()
    arr.append(sum(int(a),int(b)))

print('--결과--')
count=1
for j in arr:
    print(count,' : ',j)
    count+=1

