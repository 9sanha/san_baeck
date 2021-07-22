# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

def limite(n,limite_num):
    if (int(n)>limite_num or int(n)<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
    else:
        return True
max=0
index=0
arr =[]
#1. 배열 안쓴것
# for i in range(9):
#     print(int(i)+1,'번째: ',end='')
#     n = int(input())
#     if(max<n):
#         max=n
#         index=int(i)+1
# print('가장 큰 수 :',max,' index:',index)

#2.배열 쓴것
for i in range(9):
    print(int(i)+1,'번째: ',end='')
    arr.append(input())
arr= list(map(int,arr))
count=1
for j in arr:
    if max<j:
        max = j
        index = count
    count+=1

print('가장 큰 수 :',max,' index:',index)

