# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def solve(N):
    count = 0
    for i in range(1,N+1): #1부터 N까지 돌려
        i = str(i)
        ok = True
        l = len(i)
        if l <= 2:
            count+=1
        else:#131
            a = int(i[1])-int(i[0])
            for j in range(1,l-1):
                c = int(i[j+1]) - int(i[j])
                if (c!=a):
                    ok = False
            if (ok):
                count+=1

    print(count)


N = int(input('정수 입력:'))

solve(N)








