# https://acmicpc.net/problem/1978
# 문제
## 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 입력
## 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 출력
## 주어진 수들 중 소수의 개수를 출력한다.

N = int(input())
M = list(map(int,input().split()))
def question(N,M):
    answer = 0
    for i in range(N):
        list_M = []
        for j in range(M[i]):
            if M[i]%(j+1) == 0:
                list_M.append(j+1)
        if len(list_M) == 2:
            answer += 1
    return answer

answer = question(N,M)
print(answer)