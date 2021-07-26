# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
#
# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
#
# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
# 사용자 최대한 고려하지 않으면서 코딩

arr = [] #[A,B,C,A*B*C]
num_count = [0 for i in range(10)] # 길이가 10인 리스트 생성 및 0으로 초기화
abc = 65 #A 아스키코드값

for i in range(3):
    print(chr(abc),':',end='')
    arr.append(int(input()))
    abc+=1

abc=0 #변수 재활용 결과 출력할 때 쓸것임
arr.append(str(arr[0]*arr[1]*arr[2])) #arr[3]에 문자형으로 곱셈 값 넣어주기

for i in range(len(arr[3])):
    n = int(arr[3][i])
    num_count[n]+=1
print('A x B x C = ',arr[3])
for i in num_count:
    print(abc,':',num_count[abc],'번')
    abc+=1