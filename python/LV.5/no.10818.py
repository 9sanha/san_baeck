# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

def limite(n,limite_num):
    if (int(n)>limite_num or int(n)<1 ):
        print('입력오류 : 입력한 숫자가 입력 범위를 벗어났습니다.(입력범위:1~',limite_num,')')
    else:
        return True
n_arr=[]
n= input('입력할 정수의 개수 입력:')
if(limite(n,1000000)):
    n_arr = input('정수 입력:').split()
    n_arr = list(map(int,n_arr))
    if(len(n_arr)==int(n)):
        max=max(n_arr)
        min=min(n_arr)
        print('가장 작은 수:',min,'가장 큰 수:',max)
    else:
        print('입력오류:정수가 ',n,'개 입력되지 않았습니다. 입력된 정수의 수 :',len(n_arr))


