# https://www.acmicpc.net/problem/2581
# 문제
## 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
## 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
## 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
## M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
## M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
## 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

M = int(input())
N = int(input())

def question(M,N):
    list_i = []
    for i in range(M,N+1):
        list_j = []
        for j in range(i):
            if i%(j+1) == 0:
                list_j.append(j)
        if len(list_j) == 2:
            list_i.append(i)
    if len(list_i) == 0:
        print(-1)
    else:
        print(sum(list_i))
        print(min(list_i))
    return 0

answer = question(M,N)
